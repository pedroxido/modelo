import json
import boto3


def lambda_handler(_, _):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Table')
    response = table.scan()
    return {
        'status_code': '200',
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
