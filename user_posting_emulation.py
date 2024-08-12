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

    """
    This class is designed to establish a connection to an AWS-hosted MySQL database using SQLAlchemy.
    """

    def __init__(self):

        """
        The database credential neccesary to connect to the database
        """

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):

        """
        Creates and returns a SQLAlchemy engine that connects to the MySQL database using the credentials and connection details provided.
        """

        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()

# Replace with your actual API Invoke URL
API_INVOKE_URL = "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/topics/0affd5f86743.user"

def json_serial(obj):

    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def post_to_kafka(data):

    """
    Posts data to a specified Kafka topic through an API endpoint.
    Usage: Sends JSON data to the Kafka topic. It prints status codes and errors if the post fails.
    """

    url = f"{API_INVOKE_URL}"
    print(url)
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data, default=json_serial))
        if response.status_code != 200:
            # print(f"Failed to post to {topic}: {response.text}")
            print(f"The status code is: {response.status_code}")
        else:
            print(f"The status code is: {response.status_code}")
    except Exception as e:
        # print(f"Error posting to {topic}: {e}")
        print('Error has occured')

def run_infinite_post_data_loop():

    """
    This function, continuously fetches random rows of data from three different database tables and posts the results to Kafka.
    Details: 
        - Loop: Runs indefinitely, fetching data at random intervals (between 0 and 2 seconds).
        - Database Queries:
            1. Queries the pinterest_data, geolocation_data, and user_data tables for random rows.
            2. Converts each result row to a dictionary.
        - Posting Data: Currently commented out, but intended to post the results to Kafka topics using the post_to_kafka function.
        - Debugging: Prints the results and status codes for monitoring.
    """
    
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

            user_res = json.dumps({
                "records": [
                    {
                    "value": user_result
                    }
                ]
            }, default=str)
            # post_to_kafka( pin_result)
            # print(f"Posted to pinterest_topic: {pin_result}")

        
            headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            
            user_response = requests.request("POST", "https://5tqlmnjg51.execute-api.us-east-1.amazonaws.com/dev/topics/0affd5f86743.user", headers=headers, data=user_res)
            print(user_response.status_code)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    





