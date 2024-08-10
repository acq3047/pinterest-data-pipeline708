# Pinterest Data Pipeline

![All text](https://github.com/acq3047/pinterest-data-pipeline708/blob/main/images/Pinterest_Logo.svg.png)

# Table of contents
1. [Description](#description)
2. [Milestone 1: Set up the environment](#milestone-1-set-up-the-environment)
    - [Usage instructions](#usage-instructions)
3. [Milestone 2: Get Started](#milestone-2-get-started)
    - [Task 1: Download the Pinterest infrastructure](#task-1-download-the-pinterest-infrastructure)
    - [Task 2: Sign in to AWS console](#task-2-sign-in-to-aws-console)
4. [Milestone 3: Batch Processing: Configure the EC2 Kafka client](#milestone-3-batch-processing-configure-the-ec2-kafka-client)
    - [Task 1: Create a .pem file locally](#task-1-create-a-pem-file-locally)
    - [Task 2: Connect to EC2 instance](#task-2-connect-to-ec2-instance)
    - [Task 3: Set up Kafka on the EC2 instance](#task-3-set-up-kafka-on-the-ec2-instance)
    - [Task 4: Create Kafka topipcs](#task-4-create-kafka-topipcs)
5. [Milestone 4: Batch Processing: Connnect a MSK cluster to a S3 bucket](#milestone-4-batch-processing-connnect-a-msk-cluster-to-a-s3-bucket)
    - [Task 1: Create a custom plugin with MSK Connect](#task-1-create-a-custom-plugin-with-msk-connect)
    - [Task 2: Create a connector with MSK Connect](#task-2-create-a-connector-with-msk-connect)
6. [Milestone 5: Batch Processing: Configuring an API in API Gateway](#milestone-5-batch-processing-configuring-an-api-in-api-gateway)
    - [Task 1: Build a Kafka REST proxy integration method for the API](#task-1-build-a-kafka-rest-proxy-integration-method-for-the-api)
    - [Task 2: Set up the Kafka REST proxy on the EC2 client](#task-2-set-up-the-kafka-rest-proxy-on-the-ec2-client)
    - [Task 3: Send data to the API](#task-3-send-data-to-the-api)
7. [Milestone 6: Batch Processing Databricks](#milestone-6-batch-processing-databricks)
    - [Task 1: Set up your databricks account](#task-1-set-up-your-databricks-account)
    - [Task 2: Mount a S3 bucket to databricks](#task-2-mount-a-s3-bucket-to-databricks)
8. [Milestone 7: Batch Processing: Spark on Databricks](#milestone-7-batch-processing-spark-on-databricks)
    - [Task 1: Clean the DataFrame that contains information about pinterest posts](#task-1-clean-the-dataframe-that-contains-information-about-pinterest-posts)
    - [Task 2: Clean the DataFrame that contains information about geolocation](#task-2-clean-the-dataframe-that-contains-information-about-geolocation)
    - [Task 3:Clean the DataFrame that contains information about users](#task-3-clean-the-dataframe-that-contains-information-about-users)
    - [Task 4: Find the most popular category in each country](#task-4-find-the-most-popular-category-in-each-country)
    - [Task 5: Find which was the most popular category each year](#task-5-find-which-was-the-most-popular-category-each-year)
    - [Task 6: Find the user with most followers in each country](#task-6-find-the-user-with-most-followers-in-each-country)
    - [Task 7: Find the most popular category for different age groups](#task-7-find-the-most-popular-category-for-different-age-groups)
    - [Task 8: Find the median follower count for different age group](#task-8-find-the-median-follower-count-for-different-age-group)
    - [Task 9: Find how many users have joined each year](#task-9-find-how-many-users-have-joined-each-year)
    - [Task 10: Find the median follower count of users based on their joining year](#task-10-find-the-median-follower-count-of-users-based-on-their-joining-year)
    - [Task 11: Find the median follower count of users based on their joining year and age group](#task-11-find-the-median-follower-count-of-users-based-on-their-joining-year-and-age-group)
9. [Milestone 8: Batch Processing: AWS MWAA](#milestone-8-batch-processing-aws-mwaa)
    - [Task 1: Create and upload a DAG to a MWAA environment](#task-1-create-and-upload-a-dag-to-a-mwaa-environment)
    - [Task 2: Trigger a DAG that runs a Databricks Notebook](#task-2-trigger-a-dag-that-runs-a-databricks-notebook)
10. [Milestone 9: Stream Processing: AWS Kinesis](#milestone-9-stream-processing-aws-kinesis)
    - [Task 1: Create data stream using Kinesis Data Stream](#task-1-create-data-stream-using-kinesis-data-stream)
    - [Task 2: Configure an API with Kinesis proxy integration](#task-2-configure-an-api-with-kinesis-proxy-integration)
    - [Task 3: Send data to the Kinesis streams](#task-3-send-data-to-the-kinesis-streams)
    - [Task 4: Read data from Kinesis Streams in Databricks](#task-4-read-data-from-kinesis-streams-in-databricks)
    - [Task 5: Transform Kinesis streams in Databricks](#task-5-transform-kinesis-streams-in-databricks)
    - [Task 6: Write the streaming data to Delta Tables](#task-6-write-the-streaming-data-to-delta-tables)




## Description

Pinterest processes billions of data points every day to enhance user experience by delivering personalized and relevant content. This data-driven approach requires a robust and scalable data pipeline capable of handling vast amounts of information in real-time. In this project, you'll build a similar system using the AWS Cloud, leveraging its powerful services to ingest, process, store, and analyze data efficiently.

By the end of this project, you will have a comprehensive understanding of how to build a scalable data pipeline similar to Pinterest's, using AWS Cloud services to manage, process, and analyze large datasets effectively.

## Milestone 1: Set up the environment

The initial phase of the project entails establishing the project repository.

At the time of creating the repository, we decided to follow the following proccedure:

![All text](https://github.com/acq3047/pinterest-data-pipeline708/blob/main/images/Set_up_the_environment.gif)

- Click on “Install Github App “ button on right panel on the Hangman project module of the AI Core portal. A new Github page will appear.
- Select the account on which you want to use for your AiCore projects
- On the next page, select the “All repositories“ checkbox.
- Click “Install & authorize“. You may be prompted to enter your password.
- Once the authorization and installation is complete, you can clone the created repository in the pyhton code editor that you have decided to use.

At the same time, we have to set up the AWS cloud. To do it, we have to hit the Create AWS Account button on the right to automatically create a new AWS cloud account.

### Usage instructions

In this section, we will outline the necessary instructions for running the project, focusing on the specific version of Python required in this project.

***Python version***
- Python version: Python 3.7 or higher

***AWS Services***
- IAM 
- EC2
- MSK

## Milestone 2: Get Started

### Task 1: Download the Pinterest infrastructure

Firstly, you need to get your hands on some infrastructure similar to that which you'd find if you were a data engineer working at Pinterest. Download the zip package from [this link](https://aicore-portal-public-prod-307050600709.s3.eu-west-1.amazonaws.com/project-files/eec4e4d1-56ca-4ce9-aa4b-bedb3c84f31f/user_posting_emulation.py). 

Inside you will find the user_posting_emulation.py, that contains the login credentials for a RDS database, which contains three tables with data resembling data received by the Pinterest API when a POST request is made by a user uploading data to Pinterest:

- **pinterest_data** contains data about posts being updated to Pinterest
- **geolocation_data** contains data about the geolocation of each Pinterest post found in pinterest_data
- **user_data** contains data about the user that has uploaded each post found in pinterest_data

Then, we have to create a separate **db_creds.yaml** file for the database credentials (HOST, USER, PASSWORD values). Add this to your **.gitignore file**, before pushing anything to GitHub, therefore ensuring you are not uploading sensitive details.

### Task 2: Sign in to AWS console

In this task, we proceed to show the proccedure to sign in in the AWS console by following a few steps that we proceed to explain below:

1. Navigate to [AWS](https://aws.amazon.com/) to sign in to the AWS Console.
2. Once you are in the AWS Console, use the following credentials to log in:
    - **Account ID**
    - **IAM user name**
    - **Password**

Once you're logged in, you will be asked to change your password. Choose a new password and make a note of it, together with your **UserId**.

You will working in the **us-east-1** region throughout this project, so always make sure to check you are in the correct region when using a new service.

## Milestone 3: Batch Processing: Configure the EC2 Kafka client

In this milestone, you will configure an **Amazon EC2 instance** to use an **Apache Kafka** client machine.

### Task 1: Create a .pem file locally

The first thing that you have to do is create a **key pair** file locally, which is a file ending in the **.pem** extension. This file will ultimately allow you to connect to your EC2 instance. To do this, first navigate to **Parameter Store** in your AWS account.

Using your **KeyPairId** (you can locate this information within the email containing your AWS login credentials) find the specific key pair associated with your EC2 instance. Select this key pair and under the **Value** field select **Show**.This will reveal the content of your key pair. Copy its entire value (including the **BEGIN** and **END** header) and paste it in the **.pem** file in VSCode.

Finally, navigate to the EC2 console and identify the instance with your unique **UserId**. Select this instance, and under the **Details** section find the **Key pair name** and make a note of this. Save the previously created file in the VSCode using the following format: **Key pair name.pem**.

### Task 2: Connect to EC2 instance

Once you have completed the previous task, you are now ready to connect to your **EC2 instance**. Follow the **Connect** instructions (**SSH client**) on the EC2 console to do this.

The SSH is a widely used protocol for connecting to remote instances using SSH key pairs. To connect to an EC2 instance via SSH, you need to have the private key associated with the key pair used during instance launch.

To connect using an SSH client:
1. Ensure you have the private key file (.pem) associated with the key pair used for the instance. This is the file you have downloaded locally when you created the EC2 instance.
2. Open the terminal on your local machine. You will need to set the the appropriate permissions for the private key file to ensure it is only accessible by the owner: chmod 400 /path/to/private_key.pem.
[All text](https://github.com/acq3047/pinterest-data-pipeline708/blob/main/images/Set_up_the_environment.gif)
3. Use the SSH command to connect to the instance. You can find the exact command to connect to your EC2 instance under Example in the SSH client tab. The command should have the following structure : ssh -i /path/to/private_key.pem ec2-user@public_dns_name. If you are already in the folder where your .pem file is located you don't need to specify the filepath.
4. When accessing the EC2 client using SSH for the first time you may encounter a message about the authenticity of the host. This message is prompted because the SSH client does not recognize the remote host and wants to verify its authenticity to ensure secure communication. You can type yes to confirm and continue connecting. By doing so, the key fingerprint will be stored in your SSH client's known_hosts file, and future connections to the same host will not prompt the same message. If during this process you are logged off the instance just run the ssh command again and you will be reconnected.

### Task 3: Set up Kafka on the EC2 instance

Your AWS account has been provided with access to an IAM authenticated MSK cluster. You don't have to create your own cluster for this project.
In order to connect to the IAM authenticated cluster, you will need to install the appropriate packages on your EC2 client machine.

1. First, install Kafka on your client EC2 machine.Don't worry about setting up the security rules for the EC2 instance to allow communication with the MSK cluster, as they have already been set up for you. Make sure to install the same version of Kafka as the one the cluster is running on (in this case 2.12-2.8.1), otherwise you won't be able to communicate with the MSK cluster.

Once inside the EC2 client we will first need to install Java by running the following command:
`sudo yum install java-1.8.0`
Then we will download Apache Kafka using the commands below:
`wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz`
`tar -xzf kafka_2.12-2.8.1.tgz`

2. Install the **IAM MSK authentication package** on your client EC2 machine. This package is necessary to connect to MSK clusters that require IAM authentication, like the one you have been granted access to.

The IAM access control allows MSK to enable both authentication and authorization for clusters. This means, that if a client tries to write something to the cluster, MSK uses IAM to check whether the client is an authenticated identity and also whether it is authorized to produce to the cluster.

To connect to a cluster that uses IAM authentication, we will need to follow additional steps before we are ready to create a topic on our client machine.

First, navigate to your Kafka installation folder and then in the **libs** folder. Inside here we will download the IAM MSK authentication package from Github, using the following command:
`wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.5/aws-msk-iam-auth-1.1.5-all.jar`

3. Before you are ready to configure your EC2 client to use AWS IAM for cluster authentication, you will need to:
    - Navigate to the **IAM console** on your AWS account
    - Here, on the left hand side select the **Roles** section
    - You should see a list of roles, select the one with the following format: **<your_UserId>-ec2-access-role**
    - Copy this role ARN and make a note of it, as we will be using it later for the cluster authentication
    - Go to the **Trust relationships** tab and select **Edit trust policy**
    - Click on the **Add a principal** button and select **IAM roles** as the Principal type
    - Replace **ARN** with the **<your_UserId>-ec2-access-role** ARN you have just copied

By following the steps above you will be able to now assume the **<your_UserId>-ec2-access-role**, which contains the necessary permissions to authenticate to the MSK cluster.

4. Configure your Kafka client to use AWS IAM authentication to the cluster. To do this, you will need to modify the **client.properties** file, inside your **kafka_folder/bin** directory accordingly.

### Task 4: Create Kafka topipcs

To create a topic, you will first need to retrieve some information about the MSK cluster, specifically: the **Bootstrap servers string** and the **Plaintext Apache Zookeeper connection string**. Make a note of these strings, as you will need them in the next step.

You will have to retrieve them using the MSK Management Console, as for this project you have not been provided with login credentials for the AWS CLI, so you will not be able to retrieve this information using the CLI.

Before running any Kafka commands, remember to make sure your **CLASSPATH** environment variable is set properly.

To set up the CLASSPATH environment variable, you can use the following command:
`export CLASSPATH=/home/ec2-user/kafka_2.12-2.8.1/libs/aws-msk-iam-auth-1.1.5-all.jar`
But make sure that the specified path is the same as on your EC2 client machine.

To verify if the CLASSPATH environment variable was set properly, you can use the echo command to display its value: **echo $CLASSPATH**.

If the CLASSPATH was set correctly, the command will output the path you assigned to it, which in your case is /home/ec2-user/kafka_2.12-2.8.1/libs/aws-msk-iam-auth-1.1.5-all.jar.

Once the **CLASSPATH** has been set properly, you can start creating the following three topics:
- **<your_UserId>**.pin for the Pinterest posts data
- **<your_UserId>**.geo for the post geolocation data
- **<your_UserId>**.user for the post user data

Where **<your_UserId>** should be replaced with the **BootstrapServerString** with the value you have obtained in the previous step.

## Milestone 4: Batch Processing: Connnect a MSK cluster to a S3 bucket

In this milestone, we proceed to set up the connection between **MSK cluster** and **S3 bucket** by using **MSK Connect** in order to make that all data going through the cluster will be automatically saved and stored in a dedicated **S3 buccket**

### Task 1: Create a custom plugin with MSK Connect

In this task we will create a custom plugin that will contain the code that defines the logic of our connector by following the steps described below.

1. Go to the S3 console and find the bucket that contains your UserId. The bucket name should have the following format: user-<your_UserId>-bucket. Make a note of the bucket name, as you will need it in the next steps.
![All text](https://github.com/acq3047/pinterest-data-pipeline708/blob/main/images/Plugin_ZIP.png)
2. On your EC2 client, download the Confluent.io Amazon S3 Connector and copy it to the S3 bucket you have identified in the previous step.

`wget https://d2p6pa21dvn84.cloudfront.net/api/plugins/confluentinc/kafka-connect-s3/versions/10.5.13/confluentinc-kafka-connect-s3-10.5.13.zip`

`aws s3 cp ./confluentinc-kafka-connect-s3-10.5.13.zip s3://user-0affd5f86743-bucket/kafka-connect-s3/ `

3. Create your custom plugin in the MSK Connect console. For this project your AWS account only has permissions to create a custom plugin with the following name: <your_UserId>-plugin. Make sure to use this name when creating your plugin.

### Task 2: Create a connector with MSK Connect

In this task, we proceed to create a connector with MSK Connect by following the following steps:

1. For this project your AWS account only has permissions to create a connector with the following name: <your_UserId>-connector. Make sure to use this name when creating your connector.
2. Make sure to use the correct configurations for your connector, specifically your bucket name should be user-<your_UserId>-bucket.
3. You should also pay attention to the topics.regex field in the connector configuration. Make sure it has the following structure: <your_UserId>.*. This will ensure that data going through all the three previously created Kafka topics will get saved to the S3 bucket.
```python
connector.class=io.confluent.connect.s3.S3SinkConnector
# same region as our bucket and cluster
s3.region=us-east-1
flush.size=1
schema.compatibility=NONE
tasks.max=3
# include nomeclature of topic name, given here as an example will read all data from topic names starting with msk.topic....
topics.regex=<YOUR_UUID>.*
format.class=io.confluent.connect.s3.format.json.JsonFormat
partitioner.class=io.confluent.connect.storage.partitioner.DefaultPartitioner
value.converter.schemas.enable=false
value.converter=org.apache.kafka.connect.json.JsonConverter
storage.class=io.confluent.connect.s3.storage.S3Storage
key.converter=org.apache.kafka.connect.storage.StringConverter
s3.bucket.name=<BUCKET_NAME>
```
4. When building the connector, make sure to choose the IAM role used for authentication to the MSK cluster in the Access permissions tab. Remember the role has the following format <your_UserId>-ec2-access-role. This is the same role you have previously used for authentication on your EC2 client, and contains all the necessary permissions to connect to both MSK and MSK Connect.

Now that you have built the plugin-connector pair, data passing through the IAM authenticated cluster, will be automatically stored in the designated S3 bucket.

## Milestone 5: Batch Processing: Configuring an API in API Gateway

To replicate the Pinterest's experimental data pipeline, you will have to build your own API. This API will send data to the MSK cluster, which in turn will be stored in an S3 bucket by using the connector created in the previous milestone.

### Task 1: Build a Kafka REST proxy integration method for the API

For this task you will not need to create your own **API**, as you have been provided with one already. The API name will be the same as your **UserId**.

1. Create a resource that allows you to build a PROXY integration for your API. To do it, you have to click on Create resource button. Select the Proxy resource toogle. For Resource Name enter **{proxy+}**. Finally, select Enable API Gateway CORS and choose Create Resource.

2. For the previously created resource, create a HTTP **ANY** method. When setting up the **Endpoint URL**, make sure to copy the correct **PublicDNS**, from the EC2 machine you have been working on in the previous milestones. Remember, this EC2 should have the same name as your UserId.

3. Deploy the API and make a note of the Invoke URL, as you will need it in a later task.

### Task 2: Set up the Kafka REST proxy on the EC2 client

Now that you have set up the Kafka REST Proxy integration for your API, you need to set up the Kafka REST Proxy on your EC2 client machine.

1. First, install the Confluent package for the Kafka REST Proxy on your EC2 client machine.
`sudo wget https://packages.confluent.io/archive/7.2/confluent-7.2.0.tar.gz`
`tar -xvzf confluent-7.2.0.tar.gz`

2. Allow the REST proxy to perform IAM authentication to the MSK cluster by modifying the **kafka-rest.properties** file.

You should now be able to see a confluent-7.2.0 directory on your EC2 instance. To configure the REST proxy to communicate with the desired MSK cluster, and to perform IAM authentication you first need to navigate to confluent-7.2.0/etc/kafka-rest. Inside here run the following command to modify the kafka-rest.properties file:

`nano kafka-rest.properties`

```python
# Sets up TLS for encryption and SASL for authN.
client.security.protocol = SASL_SSL

# Identifies the SASL mechanism to use.
client.sasl.mechanism = AWS_MSK_IAM

# Binds SASL client implementation.
client.sasl.jaas.config = software.amazon.msk.auth.iam.IAMLoginModule required awsRoleArn="Your Access Role";

# Encapsulates constructing a SigV4 signature based on extracted credentials.
# The SASL client bound by "sasl.jaas.config" invokes this class.
client.sasl.client.callback.handler.class = software.amazon.msk.auth.iam.IAMClientCallbackHandler
```

3. Start the REST proxy on the EC2 client machine.

Before sending messages to the API, in order to make sure they are consumed in MSK, we need to start our REST proxy. To do this, first navigate to the confluent-7.2.0/bin folder, and then run the following command:

`./kafka-rest-start /home/ec2-user/confluent-7.2.0/etc/kafka-rest/kafka-rest.properties`

### Task 3: Send data to the API

Now, we proceed to send the data to the API, which in turn will send the data to the MSK Cluster using the plugin-connector pair previously created.

1. Modify the **user_posting_emulation.py** to send data to your Kafka topics using your API Invoke URL. You should send data from the three tables to their corresponding Kafka topic.

2. Check data is sent to the cluster by running a Kafka consumer (one per topic). If everything has been set up correctly, you should see messages being consumed.

3. Check if data is getting stored in the S3 bucket. Notice the folder organization (e.g **topics/<your_UserId>.pin/partition=0/**) that your connector creates in the bucket. Make sure your database credentials are encoded in a separate, hidden **db_creds.yaml** file.

## Milestone 6: Batch Processing Databricks

In this task, we proceed to set up a Databricks account and read data from AWS.

### Task 1: Set up your databricks account

In this task, you have to creat your Databricks account. To do it, you have to go to Databricks website and create your account.

### Task 2: Mount a S3 bucket to databricks

In order to clean and query your batch data, you will need to read this data from your S3 bucket into Databricks. To do this, you will need to mount the desired S3 bucket to the Databricks account. The Databricks account you have access to has already been granted full access to S3, so you will not need to create a new **Access Key** and **Secret Access Key** for Databricks. The credentials have already been uploaded to Databricks for you. You will only need to read in the data from the Delta table, located at **dbfs:/user/hive/warehouse/authentication_credentials**.

When reading in the JSONs from S3, make sure to include the complete path to the **JSON** objects, as seen in your S3 bucket (e.g **topics/<your_UserId>.pin/partition=0/**).


You should create three different DataFrames:

- **df_pin** for the Pinterest post data
- **df_post** for the Pinterest geolocation data
- **df_user** for the Pinterest user data

## Milestone 7: Batch Processing: Spark on Databricks

In this milestone, we will explore how to perform data claning and computations using SPARK on Databricks.

### Task 1: Clean the DataFrame that contains information about pinterest posts

To clean the **df_pin** DataFrame you should perform the following transformations:

Replace empty entries and entries with no relevant data in each column with **Nones**
Perform the necessary transformations on the **follower_count** to ensure every entry is a number. Make sure the data type of this column is an **int**.
Ensure that each column containing numeric data has a numeric data type
Clean the data in the save_location column to include only the save location path
Rename the index column to **ind**.
Reorder the DataFrame columns to have the following column order:
- **ind**
- **unique_id**
- **title**
- **description**
- **follower_count**
- **poster_name**
- **tag_list**
- **is_image_or_video**
- **image_src**
- **save_location**
- **category**

### Task 2: Clean the DataFrame that contains information about geolocation

To clean the df_geo DataFrame you should perform the following transformations:

Create a new column **coordinates** that contains an array based on the **latitude** and **longitude** columns
Drop the **latitude** and **longitude** columns from the DataFrame
Convert the **timestamp** column from a string to a timestamp data type
Reorder the DataFrame columns to have the following column order:
- **ind**
- **country**
- **coordinates**
- **timestamp**

### Task 3: Clean the DataFrame that contains information about users

To clean the **df_user** DataFrame you should perform the following transformations:

Create a new column **user_name** that concatenates the information found in the **first_name** and **last_name** columns
Drop the **first_name** and **last_name** columns from the DataFrame
Convert the **date_joined** column from a string to a timestamp data type
Reorder the DataFrame columns to have the following column order:
- **ind**
- **user_name**
- **age**
- **date_joined**

### Task 4: Find the most popular category in each country

Find the most popular Pinterest category people post to based on their country.

Your query should return a DataFrame that contains the following columns:
- **country**
- **category**
- **category_count**, a new column containing the desired query output

### Task 5: Find which was the most popular category each year

Find how many posts each category had between 2018 and 2022.

Your query should return a DataFrame that contains the following columns:
- **post_year**, a new column that contains only the year from the **timestamp** column
- **category**
- **category_count**, a new column containing the desired query output by using the same apprach as in **Task 5**

### Task 6: Find the user with most followers in each country

1. For each country find the user with the most followers.


Your query should return a DataFrame that contains the following columns:
- **country**
- **poster_name**
- **follower_count**

2. Based on the above query, find the country with the user with most followers.


Your query should return a DataFrame that contains the following columns:
- **country**
- **follower_count**

This DataFrame should have only one entry.

### Task 7: Find the most popular category for different age groups

What is the most popular category people post to based on the following age groups:
- 18-24
- 25-35
- 36-50
- +50
Your query should return a DataFrame that contains the following columns:
- **age_group**, a new column based on the original age column
- **category**
- **category_count**, a new column containing the desired query output as in **Task 5**

### Task 8: Find the median follower count for different age group

What is the median follower count for users in the following age groups:
- 18-24
- 25-35
- 36-50
- +50

Your query should return a DataFrame that contains the following columns:
- **age_group**, a new column based on the original **age** column
- **median_follower_count**, a new column containing the desired query output

### Task 9: Find how many users have joined each year

Find how many users have joined between 2015 and 2020.

Your query should return a DataFrame that contains the following columns:
- **post_year**, a new column that contains only the year from the **timestamp** column
- **number_users_joined**, a new column containing the desired query output

### Task 10: Find the median follower count of users based on their joining year

Find the median follower count of users have joined between 2015 and 2020.

Your query should return a DataFrame that contains the following columns:
- **post_year**, a new column that contains only the year from the **timestamp** column
- **median_follower_count**, a new column containing the desired query output

### Task 11: Find the median follower count of users based on their joining year and age group

Find the median follower count of users that have joined between 2015 and 2020, based on which age group they are part of.

Your query should return a DataFrame that contains the following columns:
- **age_group**, a new column based on the original **age** column
- **post_year**, a new column that contains only the year from the **timestamp** column
- **median_follower_count**, a new column containing the desired query output

## Milestone 8: Batch Processing: AWS MWAA

In this task, you will proceed to orchestrate the Databricks Workloads on **AWS MWAA**

### Task 1: Create and upload a DAG to a MWAA environment

Your AWS account has been already been provided with access to a MWAA environment **Databricks-Airflow-env** and to its S3 bucket **mwaa-dags-bucket**. Thus, you will not be required to create an API token in Databricks to connect to your AWS account, to set up the MWAA-Databricks connection or to create the **requirements.txt** file.

You will only need to create an Airflow DAG that will trigger a Databricks Notebook to be run on a specific schedule. This DAG should be uploaded to the **dags** folder in the **mwaa-dags-bucket**.

Your AWS account has been granted permissions to upload and update the following file **<your_UserId_dag.py>** to the **mwaa-dags-bucket**. Make sure to give your DAG the correct name, otherwise you will run into permission errors. Be careful to also name the DAG inside the **<your_UserId_dag.py>** as such: **<your_UserId_dag>**. You should schedule the DAG to run daily.

### Task 2: Trigger a DAG that runs a Databricks Notebook

Manually trigger the DAG you have uploaded in the previous step and check it runs successfully.

## Milestone 9: Stream Processing: AWS Kinesis

The objective of this milestone is stream data through Kinesis and read it in Databricks

### Task 1: Create data stream using Kinesis Data Stream

Using Kinesis Data Streams create three data streams, one for each Pinterest table.

Create and describe the following streams:
- streaming-<your_UserId>-pin
- streaming-<your_UserId>-geo
- streaming-<your_UserId>-user

Make sure you follow the correct nomenclature, otherwise you will run into permission errors when creating the streams.

### Task 2: Configure an API with Kinesis proxy integration

Configure your previously created REST API to allow it to invoke Kinesis actions. Your AWS account has been granted the necessary permissions to invoke Kinesis actions, so you will not need to create an IAM role for your API to access Kinesis.

The access role you have been provided with has the following structure: **<your_UserId-kinesis-access-role>**. You can copy the ARN of this role from the IAM console, under Roles. This is the ARN you should be using when setting up the **Execution role** for the integration point of all the methods you will create.

Your API should be able to invoke the following actions:
- List streams in Kinesis
- Create, describe and delete streams in Kinesis
- Add records to streams in Kinesis

### Task 3: Send data to the Kinesis streams

Create a new script **user_posting_emulation_streaming.py**, that builds upon the initial ****user_posting_emulation.py** you have been provided with.

In this script, you should send requests to your API, which adds one record at a time to the streams you have created. You should send data from the three Pinterest tables to their corresponding Kinesis stream.

Make sure your database credentials are encoded in a separate, hidden **db_creds.yaml file**.

### Task 4: Read data from Kinesis Streams in Databricks

1. Create a new Notebook in Databricks and read in your credentials from the Delta table, located at **dbfs:/user/hive/warehouse/authentication_credentials**, to retrieve the **Access Key** and **Secret Access Key**. Follow the same process for this, as you have followed for your batch data.

2. Run your preferred method to ingest data into Kinesis Data Streams. In the Kinesis console, check your data streams are receiving the data.

3. Read the data from the three streams you have created in your Databricks Notebook.

### Task 5: Transform Kinesis streams in Databricks

Clean the streaming data in the same way you have previously cleaned the batch data.

### Task 6: Write the streaming data to Delta Tables

Once the streaming data has been cleaned, you should save each stream in a Delta Table. You should save the following tables: **<your_UserId>_pin_table**, **<your_UserId>_geo_table** and **<your_UserId>_user_table**.