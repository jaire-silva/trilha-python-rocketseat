from rabbitmq_projeto_carteiro.src.main.rabbitmq_configs.consumer import RabbitMQConsumer
from rabbitmq_projeto_carteiro.publisher import RabbitMQPublisher

if __name__ == '__main__':
    publisher = RabbitMQPublisher()
    publisher.send_message({"message": "Hello, RabbitMQ!"})
    publisher.close()

    consumer = RabbitMQConsumer()
    consumer.start()
