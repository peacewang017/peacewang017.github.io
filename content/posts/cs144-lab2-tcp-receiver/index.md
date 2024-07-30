+++
title = 'Cs144 Lab2 Tcp Receiver'
date = 2024-07-24T11:05:11+08:00
draft = true
category = "study"
tags = ["network", "TCP"]
+++

# 1 Overview
前面已经实现了 ByteStream 和 Reassembler，这里实现的 TCPReceiver 将会通过 receive() 接受 TCPSender 发送的信息，调用 Reassembler，最终将有序字节传入 ByteStream。

...
