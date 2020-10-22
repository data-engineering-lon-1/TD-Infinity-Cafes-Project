import csv
import json
import boto3

def read_data_from_s3(event):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_and_key = event["Records"][0]["s3"]["object"]["key"]
    s3 = boto3.client("s3")
    # all_s3_objects = s3.list_objects(Bucket = bucket) 
    
    
    data = s3.get_object(Bucket=bucket, Key=s3_and_key)
    data = data['Body'].read().decode('utf-8').split("\n")
    
    reader = csv.reader(data)
    
    return list(reader)