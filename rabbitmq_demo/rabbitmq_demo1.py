#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pika


def send_msg():
    username = 'admin'  # 指定远程rabbitmq的用户名密码
    pwd = 'admin'
    user_pwd = pika.PlainCredentials(username, pwd)
    connection_info = pika.ConnectionParameters(host='192.168.1.61', port=5672, credentials=user_pwd)
    connection = pika.BlockingConnection(connection_info)  # 定义连接池
    channel = connection.channel()  # 声明队列以向其发送消息消息
    channel.queue_declare(queue='test_persistent', durable=True)
    for i in range(1000):
        channel.basic_publish(exchange='', routing_key='test_persistent', body=str(i),
                              properties=pika.BasicProperties(delivery_mode=2))
        print('send success msg[%s] to rabbitmq' % i)
    connection.close()  # 关闭连接
    channel.de


if __name__ == '__main__':
    send_msg()
