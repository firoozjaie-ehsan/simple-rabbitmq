# simple-rabbitmq

This is a simple example project demonstrating **RabbitMQ** usage with **Python** and **Docker**.  
It includes a Python producer (`send.py`) and consumer (`receive.py`) that communicate via RabbitMQ queues.

---

## Features

- Producer (send.py) to send messages to a queue.
- Consumer (receive.py) to receive messages from the queue.
- Dockerized environment for both RabbitMQ and Python application.
- Retry mechanism in Python to handle RabbitMQ connection delays.
- Simple folder structure for easy extension.

---

## Project Structure

- `app/`: Contains Python scripts for sending and receiving messages.
- `connections/`: Handles RabbitMQ connection and channel setup.
- `docker-compose.yml`: Docker Compose setup for RabbitMQ and Python container.
- `requirements.txt`: Python dependencies (e.g., `pika`).
- `run.sh`: Optional script to run producer and consumer.

---

## Setup & Usage

1. **Build and start containers**

```bash
docker compose --env-file .env.test up --build


2. ** Run the producer ( send messages )  **

```bash
docker exec -it -e PYTHONPATH=/app python_test python app/send.py



3. ** Run the consumer ( receive messages )  **

```bash
docker exec -it -e PYTHONPATH=/app python_test python app/receive.py

---

## Features

RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_USER=admin
RABBITMQ_PASS=admin
RABBITMQ_VHOST=/
RUN_MODE=test
