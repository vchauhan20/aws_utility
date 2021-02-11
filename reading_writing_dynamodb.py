import boto3

# setting up a client

client = boto3.client('dynamodb')


# dictionary format for reading or writing to dynamodb

item = { 'name_of_column':{'datatype':'value'},
         'name_of_second_column':{'datatype':'value'}
         }

# Writing to dynamoDb

client.put_item(TableName = 'Nameofthe table',Item = item)

# reading from database

result = client.get_item(TableName = 'Name_of_table',key =item)

