from src.transform import transform_rows
from src.load import load_by_row
from src.extract import read_data_from_s3, extract_from_csv
import json


def etl(event, context):
    data = read_data_from_s3(event)
    print("Raw", data[0])
    # data = extract_from_csv("test_data.csv")
    t_data = transform_rows(data)
    print("Transformed", t_data[0])
    load_by_row(t_data)


# event = {
#     "Records": [
#         {
#             "eventVersion": "2.0",
#             "eventSource": "aws:s3",
#             "awsRegion": "eu-west-1",
#             "eventTime": "1970-01-01T00:00:00.000Z",
#             "eventName": "ObjectCreated:Put",
#             "userIdentity": {
#                 "principalId": "EXAMPLE"
#             },
#             "requestParameters": {
#                 "sourceIPAddress": "127.0.0.1"
#             },
#             "responseElements": {
#                 "x-amz-request-id": "EXAMPLE123456789",
#                 "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
#             },
#             "s3": {
#                 "s3SchemaVersion": "1.0",
#                 "configurationId": "testConfigRule",
#                 "bucket": {
#                     "name": "teamdatum1",
#                     "ownerIdentity": {
#                         "principalId": "EXAMPLE"
#                     },
#                     "arn": "arn:aws:s3:::example-bucket"
#                 },
#                 "object": {
#                     "key": "testdata2.csv",
#                     "size": 1024,
#                     "eTag": "0123456789abcdef0123456789abcdef",
#                     "sequencer": "0A1B2C3D4E5F678901"
#                 }
#             }
#         }
#     ]
# }

# etl(event)
