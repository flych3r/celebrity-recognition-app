import logging
import boto3
import hashlib
import time
from botocore.exceptions import ClientError


def upload_file(object, bucket, object_name=None, object_ext=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: Object data if successful, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        seed = str(time.time())
        object_name = hashlib.sha1(str.encode(seed)).hexdigest()
        if object_ext:
            object_name = '{}.{}'.format(object_name, object_ext)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_fileobj(object, bucket, object_name)
        return response
    except ClientError as e:
        logging.error(e)
        return False
