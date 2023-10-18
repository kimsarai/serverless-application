import boto3
import json

def lambda_handler(event, context):
    
    dynamoDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamoDB.Table('count-table')
    
    response = table.get_item(
        Key={
            'name': event['queryStringParameters']['name']
        }
    )
    

    if event['queryStringParameters']['name'] == response['Item']['name']:

        table.update_item(
            Key={'name': response['Item']['name']},
            UpdateExpression='set accessNumber = :s',
            ExpressionAttributeValues={
                ':s' : response['Item']['accessNumber'] + 1
            },
        )

        return {"statusCode": 200, "body": int(response['Item']['accessNumber'] + 1)}