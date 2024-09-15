from fastapi import FastAPI
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "common")))
from db_handler import query_table, insert_entry
from status_codes import STATUS_CODES
from kafka_handler import produce_update

app = FastAPI()

@app.get("/post/ip/{ip_address}")
def post_ip(ip_address: str):
    status = insert_entry(ip_address, "{}")

    if status is STATUS_CODES.OK:
        produce_update(ip_address)
        return status, "SUCCEDED"
    elif status is STATUS_CODES.ERROR:
        return status, "ERROR"
    else:
        return "unknown error"
   



@app.get("/get/json/{ip_address}")
def get_json(ip_address: str):
    # Here you can add logic to fetch or generate JSON data for the given IP address
    # For demonstration, returning a simple JSON response
    return {"ip_address": ip_address, "data": "Sample data for IP"}


@app.get("/get/all")
def get_all():
    status, output = query_table()
    return output
# To run the application, use the command: uvicorn filename:app --reload


if __name__ == "__main__":
    print(get_all())
    print(post_ip("1.1.1.1"))
    print(get_all())