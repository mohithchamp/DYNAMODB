import json
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'Vesrionstore'
table = dynamodb.Table(table_name)

def processS3Object(event, context):
    print('Received event:', json.dumps(event, indent=2))

    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    
    try:
        print('Code started')
        response = s3.get_object(Bucket=bucket, Key=key)
        data = response['Body'].read().decode('utf-8')
        print('Data from S3:', data)

        items = json.loads(data)
        print(f'Processing {len(items)} items.')

        chunks = [items[i:i + 1000] for i in range(0, len(items), 1000)]

        for chunk in chunks:
           put_requests = [{'PutRequest': {'Item': item}} for item in chunk]

           batch_params = {'Vesrionstore': put_requests}  # Use the table name as the key
    
           dynamodb.batch_write_item(RequestItems=batch_params)

        print(f'Inserted {len(chunk)} items into DynamoDB.')


        return {
            'statusCode': 200,
            'body': json.dumps('Data inserted successfully')
        }
    except Exception as e:
        print('Error:', str(e))

        return {
            'statusCode': 500,
            'body': json.dumps('Error inserting data')
        }
