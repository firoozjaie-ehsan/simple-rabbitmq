#!/usr/bin/env python
import pika
from connections.rabbitmq_connection import get_connection


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

connection = get_connection()
channel = connection.channel()

# صف درخواست‌های RPC
channel.queue_declare(queue="rpc_queue")


def on_request(ch, method, props, body):
    n = int(body)
    print(f" [.] fib({n})")

    response = fib(n)

    # ارسال پاسخ به صفی که client مشخص کرده
    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id,
        ),
        body=str(response),
    )

    # اعلام می‌کنیم که پیام مصرف شد
    ch.basic_ack(delivery_tag=method.delivery_tag)


# برای اینکه فقط یک پیام در لحظه پردازش کنیم
channel.basic_qos(prefetch_count=1)

# مصرف از صف RPC
channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
