# Dynamodb_Project
Load data from s3 to dynamo db

Steps to Load the data
- Please install serverless package golbally by running "npm install serverless -g" command
- Configure the AWS account using cmd 
    - using command "aws configure"
    - provide access key and sceret access key
    - provide default region and output format
- Create a dynamodb table with the attributes required
- Run pip  install boto3 moto to install the required libraries.
- In terminal, run command "serverless deploy", this will create the couldoformation template and get deployed on the configured aws account.
- Once the s3 bucket is created make the bucket public(not a good practice), so that the lambda can access the files from s3.


-with these steps, we are all set to upload the file to s3 and it will trigger the lambda to push data to dynamo db.
