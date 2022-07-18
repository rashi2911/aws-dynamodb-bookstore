import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('Books')

# The UpdateItem API allows you to update a particular item as identified by its key.
resp = table.update_item(
    Key={"Author": "John Grisham", "Title": "The Rainmaker"},
    ExpressionAttributeNames={
        "#formats": "Formats",
        "#audiobook": "Audiobook",
    },
    ExpressionAttributeValues={
        ":id": "8WE3KPTP",
    },
    # UpdateExpression declares the updates you want to perform on your item.
    UpdateExpression="SET #formats.#audiobook = :id",
)
