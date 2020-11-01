import csv
import json
import boto3


def read_data_from_s3(event):
    s3_event = event["Records"][0]["s3"]
    bucket = s3_event["bucket"]["name"]
    s3_and_key = s3_event["object"]["key"]

    s3 = boto3.resource("s3")
    s3_object = s3.Object(bucket, s3_and_key)

    data = s3_object.get()["Body"].read().decode("utf-8").splitlines()
    reader = csv.reader(data)

    raw = []
    for row in reader:
        raw.append(row)

    return raw