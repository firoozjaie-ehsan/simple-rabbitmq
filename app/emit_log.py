#!/usr/bin/env python
import sys
from connections import rabbitmq_connection

print(" [*] Connecting to RabbitMQ")

channel = rabbitmq_connection.get_channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

message = " ".join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange="logs", routing_key="", body=message)
print(f" [x] Sent {message}")

channel.close()