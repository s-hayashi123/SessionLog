from db import table, to_decimal
from boto3.dynamodb.conditions import Key


def get_member_sessions(member_id: str):
    res = table.query(
        KeyConditionExpression=Key("PK").eq(f"member#{member_id}")
        & Key("SK").begins_with("session#"),
        ScanIndexForward=False,
    )
    return res["Items"]


def create_session(member_id: str, session_date: str, data: dict):
    table.put_item(
        Item={
            "PK": f"member#{member_id}",
            "SK": f"session#{session_date}",
            "session_date": session_date,
            **to_decimal(data),
        }
    )


def get_session_details(member_id: str, session_date: str):
    res = table.query(
        KeyConditionExpression=Key("PK").eq(f"member#{member_id}")
        & Key("SK").begins_with(f"detail#{session_date}")
    )
    return res["Items"]


def create_session_detail(
    member_id: str, session_date: str, exercise_id: str, data: dict
):
    table.put_item(
        Item={
            "PK": f"member#{member_id}",
            "SK": f"detail#{session_date}#exercise#{exercise_id}",
            "exercise_member": f"member#{member_id}#exercise#{exercise_id}",
            **to_decimal(data),
        }
    )


def update_session(member_id: str, session_date: str, data: dict):
    data = to_decimal(data)
    attr_names = {f"#k{i}": k for i, k in enumerate(data)}
    expr_values = {f":v{i}": v for i, (k, v) in enumerate(data.items())}
    update_expr = "SET " + ", ".join(f"#k{i} = :v{i}" for i, k in enumerate(data))
    table.update_item(
        Key={"PK": f"member#{member_id}", "SK": f"session#{session_date}"},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=attr_names,
        ExpressionAttributeValues=expr_values,
    )
