import logging
import random
import boto3
from botocore.exceptions import ClientError
​
​
​
def create_bucket(bucket_name=None, region=None):
    """Create an S3 bucket in a specified region
​
    If a bucket name is not specified, the bucket name will be rekog-s3-xxxxxx
    where xxxxxx is a random between 100000 & 999999
    
    If a region is not specified, the bucket is created in the S3
    region eu-east-1
    ie. EU(London).
​
    :param bucket_name: Bucket to create, e.g., 'unique-bucketname'
    :param region: String region to create bucket in, e.g., 'eu-west-2'
    :return: True if bucket created, else False
​
    version 1.1 can check bucket name format and the region entered are valid
​
​
    """
​
​
​
    # Create bucket
    if bucket_name is None:
        rnd = random.randint(100000, 999999)
        bucket_name = ("rekog-s3-"+str(rnd))
        print (bucket_name)
​
    if region is None:
            region = "eu-west-2"
    
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
