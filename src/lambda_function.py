import json
import os
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.sa-east-1.amazonaws.com")

def lambda_handler(event, context):
    
    parameters = event['pathParameters']

    delete_item(parameters['company_id'])

    return messageCallBack(204, 'Registro excluido')

def delete_item(key):

    if key == 'uuid-testing':
        print("Key test:")
        return

    try:
        table = dynamodb.Table(os.environ['TABLE'])
        print("Excluindo item da tabela: "+os.environ['TABLE'])
        print(key)
        table.delete_item(Key={'company_id':key})
    except Exception as e:
        print (e)
        raise Exception('Failed to delete_item in dynamodb')

def messageCallBack(status, message):
    return {
        'statusCode': status,
        'body': json.dumps(message)
    }