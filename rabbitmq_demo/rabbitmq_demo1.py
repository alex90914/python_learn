#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pika
import queue


def send_msg():
    username = 'admin'  # 指定远程rabbitmq的用户名密码
    pwd = 'admin'
    user_pwd = pika.PlainCredentials(username, pwd)
    connection_info = pika.ConnectionParameters(host='node01', port=5672, credentials=user_pwd)
    connection = pika.BlockingConnection(connection_info)  # 定义连接池
    channel = connection.channel()  # 声明队列以向其发送消息消息
    channel.queue_declare(queue='test_persistent', durable=True)
    for i in range(1000):
        channel.basic_publish(exchange='', routing_key='test_persistent', body=str(i),
                              properties=pika.BasicProperties(delivery_mode=2))
        print('send success msg[%s] to rabbitmq' % i)
    connection.close()  # 关闭连接


def callback(ch, method, properties, body):
    print('[x] Received %r' % body)


def recv_msg():
    username = 'admin'  # 指定远程rabbitmq的用户名密码
    pwd = 'admin'
    user_pwd = pika.PlainCredentials(username, pwd)
    connection_info = pika.ConnectionParameters(host='node01', port=5672, credentials=user_pwd)
    connection = pika.BlockingConnection(connection_info)  # 定义连接池
    channel = connection.channel()  # 声明队列以向其发送消息消息
    channel.queue_declare(queue='test_persistent', durable=True)
    channel.basic_consume("test_persistent", callback)
    channel.start_consuming()


if __name__ == '__main__':
    # send_msg()
    recv_msg()
