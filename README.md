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
