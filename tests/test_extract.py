import sys
sys.path.append(".")
import unittest
from src.extract import read_data_from_s3
import csv
import json
import boto3

class TestExtract(unittest.TestCase):
    def setUp(self):
        self.test_event = {
            "Records": [
                {
                    "eventVersion": "2.0",
                    "eventSource": "aws:s3",
                    "awsRegion": "eu-west-1",
                    "eventTime": "1970-01-01T00:00:00.000Z",
                    "eventName": "ObjectCreated:Put",
                    "userIdentity": {
                        "principalId": "EXAMPLE"
                    },
                    "requestParameters": {
                        "sourceIPAddress": "127.0.0.1"
                    },
                    "responseElements": {
                        "x-amz-request-id": "EXAMPLE123456789",
                        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
                    },
                    "s3": {
                        "s3SchemaVersion": "1.0",
                        "configurationId": "testConfigRule",
                        "bucket": {
                            "name": "teamdatum1",
                            "ownerIdentity": {
                                "principalId": "EXAMPLE"
                            },
                            "arn": "arn:aws:s3:::example-bucket"
                        },
                        "object": {
                            "key": "testdata2.csv",
                            "size": 1024,
                            "eTag": "0123456789abcdef0123456789abcdef",
                            "sequencer": "0A1B2C3D4E5F678901"
                        }
                    }
                }
            ]
        }

        self.expected_result = [['16/10/2020 09:00', 'Notting Hill', 'Otis Scott', ',Red Label tea,1.2,,Cortado,2.05,Large,Latte,2.45', 'CASH', '5.7', 'None'], ['16/10/2020 06:00', 'Camden Town', 'Phillip Hall', ',Smoothies - Glowing Greens,2.0,Regular,Espresso,1.5', 'CARD', '3.5', 'americanexpress,355466895957268'], ['16/10/2020 08:00', 'South Bank', 'Tom Daly', 'Large,Espresso,1.8,,Smoothies - Carrot Kick,2.0,,Smoothies - Carrot Kick,2.0,,Speciality Tea - Earl Grey,1.3',
                                                                                                                                                                                                                                                                                                                                'CARD', '7.1', 'visa16,4477451298311961'], ['16/10/2020 06:00', 'Westminster', 'John Smith', ',Red Label tea,1.2', 'CASH', '1.2', 'None'], ['16/10/2020 09:01', 'Notting Hill', 'Corinne Bell', ',Flavoured iced latte - Vanilla,2.75,Large,Americano,2.25,,Mocha,2.3,Large,Americano,2.25,,Speciality Tea - Peppermint,1.3', 'CARD', '10.85', 'americanexpress,348128192291466']]

    def tearDown(self):
        print("\nFinished testing - resource warning is due to boto3 connection and closes after idle time.")

    def test_read_data_from_s3(self):
        expected = self.expected_result
        actual = read_data_from_s3(self.test_event)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
