import boto3
import random
import time
from decimal import Decimal

# Initialize the DynamoDB resource
# dynamodb = boto3.resource('dynamodb')
session = boto3.Session(profile_name='default', region_name='ap-south-1')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('order_table')

def mock_data_generator():
    order_ID = str(random.randint(1, 1000000))
    product_name = random.choice([['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger']])
    quantity = random.randint(1, 5)
    price = Decimal(str(round(random.uniform(10.0, 500.0), 2)))

    return {
        'orderid': order_ID,
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }


def inserted_into_dynamoDB():
    try:
        table.put_item(Item=data)
        print(f"Inserted data: {data}")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")


if __name__ == '__main__':
    try:
        while True:
            data = mock_data_generator()
            inserted_into_dynamoDB()
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nScript stopped by manual intervention!")