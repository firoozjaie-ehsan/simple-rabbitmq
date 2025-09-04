from connections import rabbitmq_connection

print(" [*] Connecting to RabbitMQ")

channel = rabbitmq_connection.get_channel()

channel.queue_declare(queue="hello")

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

channel.basic_consume(
    queue="hello",
    on_message_callback=callback,
    auto_ack=True,
)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()



# auto_ack=True
# به محض دریافت پیام اکنالج میفرسته و از صف حذف میکنه 