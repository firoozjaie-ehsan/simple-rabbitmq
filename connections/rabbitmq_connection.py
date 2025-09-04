import os
import time
import pika

def get_connection():
    username = os.environ.get("RABBITMQ_USER", "guest")
    password = os.environ.get("RABBITMQ_PASS", "guest")
    host = os.environ.get("RABBITMQ_HOST", "rabbitmq")
    port = int(os.environ.get("RABBITMQ_PORT", 5672))
    vhost = os.environ.get("RABBITMQ_VHOST", "/")
    print(f"[*] Connecting to RabbitMQ -> Host: {host}  Port: {port},  User: {username} , VHost: {vhost} , pass: {password}")

    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(
        host=host,
        port=port,
        virtual_host=vhost,
        credentials=credentials,
    )

    # Retry loop
    for i in range(10):
        try:
            print(f"[*] Trying to connect to RabbitMQ ({i+1}/10)...")
            return pika.BlockingConnection(parameters)
        except pika.exceptions.AMQPConnectionError:
            time.sleep(2)
    raise Exception("Cannot connect to RabbitMQ after 10 retries")

def get_channel():
    connection = get_connection()
    return connection.channel()

