import boto3

client = boto3.client('s3')
bucketName = 'sayantan-demo-boto3-s3'   

# check if bucket is empty
response = client.list_objects_v2(
    Bucket='sayantan-demo-boto3-s3',
)

if not 'Contents' in response:

    response = client.delete_bucket(
        Bucket=bucketName,      
    )   # for deleting the bucket

    print(f"{ bucketName } is deleted")
else:
    print(f"{ bucketName } is not empty.")


