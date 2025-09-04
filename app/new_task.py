import sys
from connections import rabbitmq_connection
import pika

channel = rabbitmq_connection.get_channel()

channel.queue_declare(queue="task_queue", durable=True)

message = " ".join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent,
    ),
)
print(f" [x] Sent {message}")

channel.close()



# sample for run 
# docker exec -it -e PYTHONPATH=/app python_test python app/new_task.py "hello word........." 