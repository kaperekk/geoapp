import pika
import sys
import os
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "common")))
from db_handler import update_JSON
from status_codes import STATUS_CODES
from model import IPAddressValidator


def read_message(message) -> tuple[str,str]:
    ip_object = IPAddressValidator(message)
    return ip_object.status, ip_object.ip

def get_JSON(ip: str) -> dict:
    return {'v': f'{random.randint(0,100)}'}

def callback(ch, method, properties, body):
    status, ip = read_message(body)
    if status == STATUS_CODES.OK:
        JSON = get_JSON(ip)
        update_status = update_JSON(JSON)
    else:
        print(f"Reading message exited with status code {status}")
    


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_consume(queue='ip_que', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
