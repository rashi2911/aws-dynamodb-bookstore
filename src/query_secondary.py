import time

import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Books')

while True:
    if not table.global_secondary_indexes or table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
        print('Waiting for index to backfill...')
        time.sleep(5)
        table.reload()
    else:
        break

resp = table.query(
    # We have used Category as an index to query data
    IndexName="CategoryIndex",
    KeyConditionExpression=Key('Category').eq('Suspense'),
)

print("The query returned the following items:")
for item in resp['Items']:
    print(item)
