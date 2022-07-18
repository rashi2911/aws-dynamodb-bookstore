import boto3
client = boto3.client('dynamodb', region_name='us-east-2')

try:
    resp = client.update_table(
        TableName="Books",
        AttributeDefinitions=[
            {
                "AttributeName": "Category",
                "AttributeType": "S"
            },
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    # You need to name your index and specifically refer to it when using it for queries.
                    "IndexName": "CategoryIndex",
                    # Like the table itself, you need to specify the key schema for an index.
                    "KeySchema": [
                        {
                            "AttributeName": "Category",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
                    }
                }
            }
        ],
    )
    print("Secondary index added!")
except Exception as e:
    print("Error updating table:")
    print(e)
