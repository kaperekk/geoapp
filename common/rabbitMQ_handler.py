import pika
import json
import random


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

def produce_update(ip: str) -> None:
    channel.basic_publish(exchange='', routing_key='ip_que', body=ip)
    connection.close()


if __name__ == "__main__":
    ip = f'{random.randint(0,10)}.{random.randint(0,10)}.{random.randint(0,10)}.{random.randint(0,10)}.{random.randint(0,10)}'
    print(ip)
    produce_update(ip)