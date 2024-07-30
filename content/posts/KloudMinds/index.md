+++
title = 'KloudMinds'
date = 2024-07-25T20:29:36+08:00
draft = true
category = "project"
tags = ["kubernetes", "docker", "python", "RAG"]
+++

# KloudMinds 项目

## 1 负责的工作

我负责的工作是 Python 中间件的开发，Kubernetes 上所有服务的部署。

## 2 基于 RabbitMQ 和 KDEA 的自动拓展

### 2.1 v1 后端直接完成对 weaviate 的操作
在 Java 后端中直接添加与 weaviate 数据库交互的模块。

这样的话:

1. 代码复用性差，拓展性差(其他模块需要与向量数据库交互逻辑的时候又得重写代码)

2. 性能差(后端需要承载切块、向量化、上传和下载的负载)

### 2.2 v2 直接通信
引入 weaviate-server，后端需要告知 retrieve-server 向 weaviate 向量数据库中上传/删除文件，在最初的实现中让后端直接给 retrieve-server 直接发送请求。

(为什么用 Python 来写: 文件的上传与下载是一件 I/O 密集型任务。也就是说，由于大部分时间并不是进行 CPU 占用，编译型语言的运行效率并不显著地更高)

这样显然会带来一些问题:

1. 代码仍然耦合性高，拓展性差(一旦有变更，后端和 server 需要同时更改)

2. 监控性差(难以实时监控后端和 retrieve-server 之间的请求强度)

### 2.3 v3 消息队列
部署 rabbitMQ 服务，改为使用消息队列通信

这样的问题是：

1. 在消息队列中的消息过多时，过少数量的 Pod 会影响文件及时上传(尽管在 Pod 内部已经尽力利用并行性)，但直接部署大量的 Pod 无疑是不合理的。

### 2.4 v4 KDEA 自动拓展
使用 KDEA (Kubernetes Event-driven Autoscaling)，监听 RabbitMQ 消息数量，自动控制 Pod 数量，满足 `Pod 数 = 消息数 / 2`

#### 2.4.1 实现方法
配置 Secret 用来存储 RabbitMQ 的连接信息

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: rabbitmq-secret
  namespace: default
type: Opaque
data:
  rabbitmq-connection-string: <Base64-encoded-RabbitMQ-connection-string>
```

部署 KDEA，配置 Scaler

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: retrieve-server-scaledobject
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: retrieve-server
  minReplicaCount: 1
  maxReplicaCount: 50
  triggers:
  - type: rabbitmq
    metadata:
      queueName: my-queue
      host: RabbitMQConnectionString
      queueLength: "2" # 每增加两条消息，就增加一个 Pod
    authenticationRef:
      name: rabbitmq-secret
```

## 3 R-A-G 功能模块
对文件进行切快，向量化后并行地传入 weaviate 响亮数据库中，在搜索的时候进行向量化匹配。

得到匹配结果后添加 prompt 调用 LLM API。

### 3.1 切块的逻辑
最初尝试使用正则匹配切割，即根据中英文句号、感叹号之类的分割符进行硬切割，发现效果不好。

改用嵌入式模型，并依据中文/英文进行不同的分割:

```python
model = SentenceTransformer('all-MiniLM-L6-v2')

spacy.cli.download("en_core_web_sm")
spacy.cli.download("zh_core_web_sm")
nlp_en = spacy.load('en_core_web_sm')
nlp_zh = spacy.load('zh_core_web_sm')

# 根据语言类型进行切快
def chunk_text(text, language='en'):
    if language == 'en':
        doc = nlp_en(text)
    else:
        doc = nlp_zh(text)
    return [sent.text.strip() for sent in doc.sents]
```

### 3.2 并行上传的逻辑
使用`concurrent.futures`模块中的`ThreadPoolExecutor`来实现并行化处理:

```python
def import_data(client, model, bucketname, filename, content, language='en'):
    chunks = chunk_text(content, language)
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, chunk, chunknum, bucketname, filename, model, client) for chunknum, chunk in enumerate(chunks)]
        for future in futures:
            future.result()
```

不用`ProcessPoolExecutor`，因为上传是 I/O 密集型任务，更适合多线程处理。

### 3.3 存放的逻辑
在向量数据库中存放四元组 

<bucketname, filename, chunknum, vectorized_content>




