import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "common")))
from db_handler import update_JSON
from status_codes import STATUS_CODES



class IPAddressValidator:
    def __init__(self, ip_str):
        self.status, self.ip = self.is_valid(ip_str)

    def is_valid(ip_str: str) -> tuple[str, str] :
        for value in ip_str.split('.'):
            if not 0 >= value > 256:
                return STATUS_CODES.ERROR, ''
        return STATUS_CODES.OK, ip_str

