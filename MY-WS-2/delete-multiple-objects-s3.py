import boto3

client = boto3.client('s3')

myBucketName = 'sayantan-demo-boto3-s3'
myKey1 = 'Messi1.jpeg'
myKey2 =  'Messi2.jpeg'

response = client.delete_objects(
    Bucket=myBucketName,
    Delete={
        'Objects': [
            {
                'Key': myKey1,
                
            },

            {
                'Key': myKey2,

            }
        ],
    },

)

print(response)

