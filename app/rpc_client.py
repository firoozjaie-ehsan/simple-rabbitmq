#!/usr/bin/env python
import uuid
from connections.rabbitmq_connection import get_connection
import pika


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = get_connection()
        self.channel = self.connection.channel()

        # ساختن یک صف موقت برای دریافت پاسخ
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        # ثبت callback برای صف پاسخ
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n),
        )
        while self.response is None:
            self.connection.process_data_events(time_limit=1)

        return int(self.response)



fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(40)")
response = fibonacci_rpc.call(40)
print(f" [.] Got {response}")
