from db import table, to_decimal
from boto3.dynamodb.conditions import Attr


def create_member(member_id: str, data: dict):
    table.put_item(
        Item={
            "PK": f"member#{member_id}",
            "SK": "profile",
            "member_id": member_id,
            **to_decimal(data),
        }
    )


def get_members():
    res = table.scan(
        FilterExpression=Attr("SK").eq("profile") & Attr("PK").begins_with("member#")
    )
    return res["Items"]


def get_member(member_id: str):
    res = table.get_item(Key={"PK": f"member#{member_id}", "SK": "profile"})
    return res.get("Item", {})


def update_member(member_id: str, data: dict):
    data = to_decimal(data)
    attr_names = {f"#k{i}": k for i, k in enumerate(data)}
    expr_values = {f":v{i}": v for i, (k, v) in enumerate(data.items())}
    update_expr = "SET " + ", ".join(f"#k{i} = :v{i}" for i, k in enumerate(data))
    table.update_item(
        Key={"PK": f"member#{member_id}", "SK": "profile"},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=attr_names,
        ExpressionAttributeValues=expr_values,
    )
