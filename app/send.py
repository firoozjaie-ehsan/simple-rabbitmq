from connections import rabbitmq_connection

print(" [*] Connecting to RabbitMQ")

channel = rabbitmq_connection.get_channel()


channel.queue_declare(queue="hello")


channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")

channel.close()