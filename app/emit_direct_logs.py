import sys

from connections import rabbitmq_connection

print(" [*] Connecting to RabbitMQ")

channel = rabbitmq_connection.get_channel()

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

severity = sys.argv[1] if len(sys.argv) > 2 else "info"
message = " ".join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(
    exchange="direct_logs",
    routing_key=severity,
    body=message,
)
print(f" [x] Sent {severity}:{message}")

channel.close()