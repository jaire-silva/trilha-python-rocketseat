import json

import pika


class RabbitMQPublisher:
    def __init__(self):
        self.__channel = None
        self.__connection = None
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = 'admin'
        self.__password = 'admin123'
        self.__exchange = 'minha_exchange'
        self.__routing_key = ''
        self.create_channel()

    def create_channel(self):
        credentials = pika.PlainCredentials(username=self.__username, password=self.__password)

        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=credentials
        )

        self.__connection = pika.Connection(connection_parameters)
        self.__channel = self.__connection.channel()


    def send_message(self, message: dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )

    def close(self):
        if self.__connection and not self.__connection.is_closed:
            self.__connection.close()


rabbit_mq_publisher = RabbitMQPublisher()
rabbit_mq_publisher.send_message({'msg': 'Estou no publisher'})
rabbit_mq_publisher.close()
