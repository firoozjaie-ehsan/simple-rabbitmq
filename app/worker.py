import time
from connections import rabbitmq_connection

import pika

channel = rabbitmq_connection.get_channel()


channel.queue_declare(queue="task_queue", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b"."))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# این خط خیلی مهم است: به ربیت می‌گوید یک وورکر در یک زمان فقط یک پیام تحویل بگیرد.
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback)

channel.start_consuming()




# ch.basic_ack(delivery_tag=method.delivery_tag)
# با این دستور بعد انجام دستور پیام اتمام داده میشه و از صف حذف میکند
# و اگر یک وورکر پیامی گرفت بعد از انجام مقداری کرش کرد ربیت کار را به وورکر دیگر میدهد
