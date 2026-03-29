import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("session-log")


def to_decimal(data: dict) -> dict:
    return {k: Decimal(str(v)) if isinstance(v, float) else v for k, v in data.items()}
