import requests
import boto3
import pytz
from datetime import datetime
import uuid
# Set your AWS credentials and region for DynamoDB
region name = 'us-east-1'|
ist = pytz. timezone('Asia/Kolkata*) # Indian Standard Time
current_time = datetime.now(ist) isoformat)
# Set your DynamoDB table namel
table_name = 'bitcoin_price storer'
# Set the REST API endpoint
api_url = 'https://api.coinbase.com/vz/prices/btc-usd/spot'
# Create a DynamoDB client
dynamodb = boto3.client("dynamodb', region_name=region_ name)
# Function to create an item in DynamoDB table
def put_item_to_dynamodbitem) :
dynamodb.put item (TableName-table name, Item item
def main():
# Fetch data from the REST API
response = requests get (api url)
data = response. json()
data_to_ingest=("amount": ("S": data["data" ][" amount "]), "base": ("S" :data["data" ]["base"]), "currency": ("S" :data["data" ]["currency"]), "timestamp": ("S": current_time), "uuid": ("S" :str
(uuid.uuid4())J}
put_item_to_dynamodb (data_to_ingest)
print (f' Item {data to ingest) added to DynamoDB table {table name).')
print( 'Data transfer complete.')