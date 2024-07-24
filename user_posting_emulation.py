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

# Replace with your actual API Invoke URL
API_INVOKE_URL = "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/topics/0affd5f86743.pin"

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def post_to_kafka(topic, data):
    url = f"{API_INVOKE_URL}/{topic}"
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data, default=json_serial))
        if response.status_code != 200:
            print(f"Failed to post to {topic}: {response.text}")
            print(f"The status code is: {response.status_code}")
        else:
            print(f"The status code is: {response.status_code}")
    except Exception as e:
        print(f"Error posting to {topic}: {e}")

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
                post_to_kafka("pinterest_topic", pin_result)
                print(f"Posted to pinterest_topic: {pin_result}")


            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)
                post_to_kafka("geolocation_topic", geo_result)
                print(f"Posted to geolocation_topic: {geo_result}")


            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
                post_to_kafka("user_topic", user_result)
                print(f"Posted to user_topic: {user_result}")
            
            print(pin_result)
            print(geo_result)
            print(user_result)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    

