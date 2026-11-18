import threading

import pika


def rabbitmq_callback(ch, method, properties, body):
    print(f" [x] Received {body}")


class RabbitMQConsumer:
    def __init__(self):
        self.__channel = None
        self.__connection = None
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = 'admin'
        self.__password = 'admin123'
        self.__queue = 'minha_queue'
        self.__routing_key = ''
        self.__stop_event = threading.Event()
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

        self.__channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        self.__channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=rabbitmq_callback
        )

    def start(self):
        print('Iniciando consumo de mensagens... Pressione CTRL+C para sair.')
        try:
            self.__stop_event.wait()
        except KeyboardInterrupt:
            print('Encerrando consumidor...')
            self.stop()

    def stop(self):
        self.__stop_event.set()
        if self.__connection and self.__connection.is_open:
            self.__connection.close()
