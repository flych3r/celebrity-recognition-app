import logging
import boto3
from botocore.exceptions import ClientError


def retrieve_all_items(table_name):
    """Retrieves all items from a dynamodb table

    :param table_name: Name of the table to get itemsied then file_name is used
    :return: Table items if successful, else False
    """

    dynamo_client = boto3.client('dynamodb')
    try:
        response = dynamo_client.scan(TableName=table_name, Select='ALL_ATTRIBUTES')
        return response['Items']
    except ClientError as e:
        logging.error(e)
        return False
