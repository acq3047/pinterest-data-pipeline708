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
PIN_API_INVOKE_URL = "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0affd5f86743-pin/record"
GEO_API_INVOKE_URL = "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0affd5f86743-geo/record"
USER_API_INVOKE_URL = "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0affd5f86743-user/record"

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def send_to_stream(data):
    # pin
    pin_url = f"{PIN_API_INVOKE_URL}"
    print(pin_url)
    pin_headers = {
        "Content-Type": "application/x-amz-json-1.1"
    }
    try:
        pin_response = requests.put(pin_url, headers=pin_headers, data=json.dumps(data, default=json_serial))
        if pin_response.status_code != 200:
            # print(f"Failed to post to {topic}: {response.text}")
            print(f"The status code is: {pin_response.status_code}")
        else:
            print(f"The status code is: {pin_response.status_code}")
    except Exception as e:
        # print(f"Error posting to {topic}: {e}")
        print('Error has occured')
    
    # geo
    geo_url = f"{GEO_API_INVOKE_URL}"
    print(geo_url)
    geo_headers = {
        "Content-Type": "application/x-amz-json-1.1"
    }
    try:
        geo_response = requests.put(geo_url, headers=geo_headers, data=json.dumps(data, default=json_serial))
        if geo_response.status_code != 200:
            # print(f"Failed to post to {topic}: {response.text}")
            print(f"The status code is: {geo_response.status_code}")
        else:
            print(f"The status code is: {geo_response.status_code}")
    except Exception as e:
        # print(f"Error posting to {topic}: {e}")
        print('Error has occured')
    
    # user
    user_url = f"{USER_API_INVOKE_URL}"
    print(user_url)
    user_headers = {
        "Content-Type": "application/x-amz-json-1.1"
    }
    try:
        user_response = requests.put(user_url, headers=user_headers, data=json.dumps(data, default=json_serial))
        if user_response.status_code != 200:
            # print(f"Failed to post to {topic}: {response.text}")
            print(f"The status code is: {user_response.status_code}")
        else:
            print(f"The status code is: {user_response.status_code}")
    except Exception as e:
        # print(f"Error posting to {topic}: {e}")
        print('Error has occured')

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
                # post_to_kafka(geo_result)
                # print(f"Posted to geolocation_topic: {geo_result}")


            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
                # post_to_kafka(user_result)
                # print(f"Posted to user_topic: {user_result}")
            
            print(user_result)
            # print(geo_result)
            # print(user_result)

            pin_playload = json.dumps({
                "StreamName": "streaming-0affd5f86743-pin",
                "Data": pin_result,
                        "PartitionKey": "partition-1"
                        }, default=str)
            
            geo_playload = json.dumps({
                "StreamName": "streaming-0affd5f86743-geo",
                "Data": geo_result,
                        "PartitionKey": "partition-1"
                        }, default=str)
            
            user_playload = json.dumps({
                "StreamName": "streaming-0affd5f86743-user",
                "Data": user_result,
                        "PartitionKey": "partition-1"
                        }, default=str)
            # post_to_kafka( pin_result)
            # print(f"Posted to pinterest_topic: {pin_result}")

        
            headers = {'Content-Type': "application/json"}
            
            # Pin response
            pin_response = requests.request("PUT", "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0affd5f86743-pin/record", headers=headers, data=pin_playload)
            print('Printing the pin_response status code')
            print(pin_response.status_code)

            # Geo response
            geo_response = requests.request("PUT", "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0affd5f86743-geo/record", headers=headers, data=geo_playload)
            print('Printing the geo_response status code')
            print(geo_response.status_code)

            # User response
            user_response = requests.request("PUT", "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/streams/streaming-0affd5f86743-user/record", headers=headers, data=user_playload)
            print('Printing the user_response status code')
            print(user_response.status_code)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    