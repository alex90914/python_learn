#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pika
import random

hostname = '192.168.1.99'
port = 5672
parameters = pika.ConnectionParameters(hostname=hostname, port=port)
connection = pika.BlockingConnection(parameters)
# 创建通道
channel = connection.channel()
# 如果rabbitmq自身挂掉的话，那么任务会丢失。所以需要将任务持久化存储起来，声明持久化存储：
queue = 'py_test_task_queue'
channel.queue_declare(queue=queue, durable=True)
number = random.randint(1, 1000)
message = 'hello world:%s' % number
# 在发送任务的时候，用delivery_mode=2来标记任务为持久化存储：
channel.basic_publish(exchange='',
                      routing_key=queue,
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      ))
print
" [x] Sent %r" % (message,)
connection.close()
