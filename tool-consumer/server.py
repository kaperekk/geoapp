import pika
import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "common")))
from db_handler import update_JSON
from status_codes import STATUS_CODES


def verify_ip(ip: str) -> str :
    return ip

def read_message(message) -> str:
    new_ip = verify_ip(message)
    return new_ip

def get_JSON(ip: str) -> dict:
    return {'v': f'{random.random()}'}

def callback(ch, method, properties, body):
    ip = read_message(body)
    JSON = get_JSON(ip)
    status = update_JSON(JSON)
    print(status)




connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_consume(queue='ip_que', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
