from db import table
from boto3.dynamodb.conditions import Key


def get_member_sessions(member_id: str):
    res = table.query(
        KeyConditionExpression=Key("PK").eq(f"member#{member_id}")
        & Key("SK").begins_with("session#")
    )
    return res["Items"]


def create_session(member_id: str, session_date: str, data: dict):
    table.put_item(
        Item={"PK": f"member#{member_id}", "SK": f"session#{session_date}", **data}
    )


def create_session_detail(
    member_id: str, session_date: str, exercise_id: str, data: dict
):
    table.put_item(
        Item={
            "PK": f"member#{member_id}",
            "SK": f"session#{session_date}#exercise#{exercise_id}",
            "exercise_member": f"member#{member_id}#exercise#{exercise_id}",
            **data,
        }
    )


def get_member_graph(member_id: str, exercise_id: str):
    res = table.query(
        IndexName="exercise-member-index",
        KeyConditionExpression=Key("exercise_member").eq(
            f"member#{member_id}#exercise#{exercise_id}"
        ),
        ScanIndexForward=True,
    )
    return res["Items"]


def get_member_body_stats(member_id: str):
    res = table.query(
        KeyConditionExpression=Key("PK").eq(f"member#{member_id}")
        & Key("SK").begins_with("session#"),
        ProjectionExpression="weight, body_fat, SK",
    )
    return res["Items"]
