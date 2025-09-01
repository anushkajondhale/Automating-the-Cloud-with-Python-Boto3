import boto3
client = boto3.client('s3')

bucketName = 'sayantan-demo-boto3-s3'

# List all the objects 
response = client.list_objects_v2(
    Bucket= bucketName,
)

# Now delete one by one in the bucket
if 'Contents' in response:
    for content in response['Contents']:
        print("Key detected: " + content['Key'])

        key=content['Key']

        client.delete_object(
            Bucket=bucketName,
            Key=key
        )
        print(f"Deleted {key}")

else:
    print("The bucket is already empty.")











# then iterate over the dictionary -- hold by 'Contents' key

# and then delete