+++
title = 'NUS Summer Workshop'
date = 2024-07-20T00:24:40+08:00
draft = false
categories = "study"
tags = ["NUS", "Cloud-computing", "Kubernetes", "Thai-food"]
+++

几个月前我刚刚来过新加坡，现在又回来了，不过不同于之前的纯旅游，这次的活动有一些 workload。

NUS summerworkshop 是 NUS SoC 每年暑假举办的活动（[项目主页](https://sws.comp.nus.edu.sg/)）, 总共时长是两个月：phase 1 阶段学生在本国内上网课，phase 2 需要到 NUS 实地完成一个现学现卖的项目，我在 12 个选项中选择了与云计算有关的 cloud-computing cluster。

# 1 住宿和饮食

在 NUS 的期间，学生会有 NUS 的学生卡、宿舍卡、定制的 EZ-LINK 交通卡等，走在校园里甚至有种自己也是 NUS 本科生的感觉。

![](image.png "校方提供的卡片")

我们住在 PGPR，很标准的学生宿舍，干净整洁。美中不足的是，因为 NUS 本科生已经放假，宿舍旁的食堂没了多少选择，我常吃印度大婶卖的沙拉配果汁，或者 supersnack 里鸡排 + 薯条 + 华夫 + 柠檬水的套餐，偶尔馋冬阴功的时候，也会走路去 NUH 的食堂，或者坐公交去 Utown：

![](image-1.png "印度大婶的沙拉")

![](image-2.png "supersnack 的鸡排套餐，柠檬水闻起来怪怪的但喝起来开胃")

![](image-3.png "supersnack 1.5新币的华夫相当饱人")

![](image-4.png "NUH 食堂的冬阴功，目前为止最喜欢的外国菜")

![](image-5.png "PGPR 宿舍")

# 2 课程和项目

## 2.1 课程
phase 2 内容主要是，用一周左右的时间理解 lecture 上老师提到的内容，并自由组队完成一个项目。

![](image-6.png "phase 2 的 timetable")

[Richard](https://richard-ma.netlify.app/) 是我们的老师，他言语和善，并且显然很认真地准备了课程。在 lecture 时，他对于 kubernetes 的部署有不少 hands-on 的操作，而非对着 PPT 朗诵。

![](image-7.png "Richard 的课堂可以称得上娓娓道来")

## 2.2 项目
我与来自北邮和川大的三位同学组队，完成了一个云原生智慧网盘应用，它拥有一个 Vue 前端、一个 Springboot 后端、一些 python 中间件，支持文件的上传、下载、分享，以及对文件内容的精确匹配 / 语义模糊匹配、基于文件的 R-A-G 等，前后端与其他组件全部通过 kubernetes 部署到 AWS 集群上。

我们在最后一天晚上云部署的过程中遇到了前后端通信异常、Mysql 数据无法持久化等问题，不过好在大家都很有干劲，最终调试出问题所在并在 DDL 前解决了！

![](image-8.png "部署出现问题且迟迟不能解决，因而熬夜到 3 点的我们 belike")

遗憾的是，在 presentation 环节，我拖了团队的后腿 -- 队友都十分信任地选我作为演讲人，但我在演讲时十分紧张甚至有些乱了阵脚，没有很好地将我们的实现与想法表达出来... 

![](image-9.png "lecture 时紧张的我")

不过无论如何，“悟以往之不谏 知来者之可追”，这次我做的不好，应该吸取教训，以后在人前做类似的报告一定要显得大方些。

## 2.3 和 Richard
在 show-case 摆海报当天，我们去与 Richard 聊了聊，关于项目的体验和建议。

![](image-10.png "与 Richard，(我是老英格兰正米字旗)")

## 2.4 和队友们
项目结束后，我们小组四人一起去海洋馆玩了一圈，并拍下了回国前的合照。

![](image-11.png "与队友们")

# 3 杂项

## 3.1 NUS SOC 的展品
![](image-12.png "NUS SOC 有不少有趣的老机器，这是其中的一台麦金塔")

## 3.2 NUS 校园
![](image-13.png "UTown 白天")

![](image-14.png "UTown 夜晚")

![](image-15.png "宿舍楼下")

![](image-16.png "经典配色巴士")