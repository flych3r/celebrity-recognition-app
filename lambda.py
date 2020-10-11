import json
import boto3
import os

CELEBS_TABLE = os.environ.get('CELEBS_TABLE')

def create_object_url(bucket_name, file_name):
    return 'https://{}.s3.amazonaws.com/{}'.format(bucket_name, file_name)

def lambda_handler(event, context):

    rekognition = boto3.client('rekognition')
    dynamo = boto3.client('dynamodb')

    if event:
        file_obj = event['Records'][0]
        bucket_name = str(file_obj['s3']['bucket']['name'])
        file_name = str(file_obj['s3']['object']['key'])
        object_url = create_object_url(bucket_name, file_name)

        response = rekognition.recognize_celebrities(
            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': file_name,
                }
            }
        )

        celebs = [celebrity['Name'] for celebrity in response['CelebrityFaces']]
        celebs = ', '.join(celebs)

        response = dynamo.put_item(
            TableName=CELEBS_TABLE,
            Item={
                'img_path': {
                    'S': object_url
                },
                'celebs': {
                    'S': celebs
                }
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
