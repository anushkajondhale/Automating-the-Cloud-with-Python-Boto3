import boto3
client = boto3.client('s3')

response = client.list_objects_v2(
    Bucket='sayantan-demo-boto3-s3',
)

# print(response) # The response is a nested dictionary structure that provides detailed information about the S3 bucket and its contents
# response['Contents'] # returns List of Dictionaries

# print(response['Contents']) 


if 'Contents' in response:
    for dict in response['Contents']:
        print(dict['Key'], dict['LastModified']) # Directly accesses the Key and LastModified fields from the Contents list in the response of the list_objects_v2 call. 
else:
    print("The bucket is already empty.")
    print("Upload objects first")
    
# for content in response['Contents']:
#     obj_dict = client.get_object(Bucket='<bucket-name>', Key=content['Key'])
#     print(content['Key'], obj_dict['LastModified'])

# it makes an additional call to client.get_object to retrieve each object's details again. 
# This is somewhat redundant since the LastModified information is already available in the Contents list from the initial list_objects_v2 call.

