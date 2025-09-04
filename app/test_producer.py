from connections import rabbitmq_connection
import pika

# گرفتن کانال
channel = rabbitmq_connection.get_channel()

# تعریف صف پایدار (همان صف worker ها)
channel.queue_declare(queue="task_queue", durable=True)

# تولید 10 پیام تستی
for i in range(1, 11):
    message = "Test Message" + "." * i
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent,  # پیام ماندگار شود
        ),
    )
    print(f" [x] Sent {message}")

channel.close()



'''
🔹 نکته خیلی مهم ⚠️

durable=True اگر فقط 
 از بین میرنRabbitMQ بزنی → صف پایدار میشه ولی پیام‌ها موقتی هستن و با ری‌استارت 


delivery_mode=Persistent اگر فقط  
بزنی → پیام پایدار هست، ولی اگه صف پایدار نباشه، کل صف با پیام‌هاش پاک میشه.

durable=True پس برای داشتن پایداری کامل هم صف باید 
باشه و هم پیام باید 
Persistent باشه.

'''
