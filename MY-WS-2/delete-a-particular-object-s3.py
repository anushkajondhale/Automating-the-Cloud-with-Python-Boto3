# to delete a particular object from your s3 bucket

import boto3

client = boto3.client('s3')


bucketName = 'sayantan-demo-boto3-s3'
keyName = 'Messi2.jpeg' # that object name that you want to delete

response = client.delete_object(
    Bucket=bucketName,
    Key=keyName )

print(response)
