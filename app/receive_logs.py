#!/usr/bin/env python
import os
import sys

from connections import rabbitmq_connection

print(" [*] Connecting to RabbitMQ")
channel = rabbitmq_connection.get_channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

def callback(ch, method, properties, body):
    print(f" [x] {body.decode()}")

print(" [*] Waiting for logs. To exit press CTRL+C")
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True,
)

channel.start_consuming()

            
            

# exclusive=True
# تا زمانی که فایل باز این صف بماند و بعد بستن حذف بشود

# queue=""           اسم رندوم خود ربیت می گذارد

#  queue_name = result.method.queue       اسم صف ایجاد شده میدهد

# وقتی تولید کننده قبل از مصرف کننده اجرا شود چون هنوز بایند نشده صف به اکسچنج پیام جایی ذخیره نمیشود