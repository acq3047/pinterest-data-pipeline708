import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
from datetime import datetime


random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()

API_URLS = {
    'UserStream': 'https://us-east-1.console.aws.amazon.com/kinesis/home?region=us-east-1#/streams/details/streaming-0affd5f86743-user',
    'GeoStream': 'https://us-east-1.console.aws.amazon.com/kinesis/home?region=us-east-1#/streams/details/streaming-0affd5f86743-geo',
    'PinStream': 'https://us-east-1.console.aws.amazon.com/kinesis/home?region=us-east-1#/streams/details/streaming-0affd5f86743-pin'
}
#API_INVOKE_URL = "https://us-east-1.console.aws.amazon.com/kinesis/home?region=us-east-1#/streams/details/streaming-0affd5f86743-pin"

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def send_to_stream(api_url, data):
    headers = {
        "Content-Type": "application/x-amz-json-1.1",
        "X-Amz-Target": "Kinesis_20131202.PutRecord"
    }
    payload = {
        "StreamName": 'stream-name',
        "Data": json.dumps(data, default=json_serial),
        "PartitionKey": str(random.randint(0, 10000))
    }
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            print(f"Failed to send to stream {api_url}: {response.text}")
        else:
            print(f"Successfully sent to stream {api_url}")
    except Exception as e:
        print(f"Error sending to stream {api_url}: {e}")


def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            #print(pin_result)
            #print(geo_result)
            #print(user_result)

            #pin_res = json.dumps({
            #    "records": [
            #        {
            #        "value": pin_result
            #        }
            #    ]
            #}, default=str)

            #geo_res = json.dumps({
            #    "records": [
            #        {
            #        "value": geo_result
            #        }
            #    ]
            #}, default=str)

            #user_res = json.dumps({
            #    "records": [
            #        {
            #        "value": user_result
            #        }
            #    ]
            #}, default=str)
            # post_to_kafka( pin_result)
            # print(f"Posted to pinterest_topic: {pin_result}")

            # Send data to respective API endpoints
            send_to_stream(API_URLS['PinStream'], pin_result)
            send_to_stream(API_URLS['GeoStream'], geo_result)  
            send_to_stream(API_URLS['UserStream'], user_result)
            #headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            
            #user_response = requests.request("PUT", "https://us-east-1.console.aws.amazon.com/kinesis/home?region=us-east-1#/streams/details/streaming-0affd5f86743-pin", headers=headers, data=pin_res)
            #print(user_response.status_code)



if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


