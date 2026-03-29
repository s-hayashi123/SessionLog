# from db import table
# from boto3.dynamodb.conditions import Key
#
#
# def get_member_goals(member_id: str):
#     res = table.query(
#         KeyConditionExpression=Key("PK").eq(f"member#{member_id}")
#         & Key("SK").begins_with("goal#")
#     )
#     return res["Items"]
#
#
# def create_goal(member_id: str, goal_id: str, data: dict):
#     table.put_item(Item={"PK": f"member#{member_id}", "SK": f"goal#{goal_id}", **data})
#
#
# def update_goal(member_id: str, goal_id: str, data: dict):
#     attr_names = {f"#k{i}": k for i, k in enumerate(data)}
#     expr_values = {f":v{i}": v for i, (k, v) in enumerate(data.items())}
#     update_expr = "SET " + ", ".join(f"#k{i} = :v{i}" for i, k in enumerate(data))
#     table.update_item(
#         Key={"PK": f"member#{member_id}", "SK": f"goal#{goal_id}"},
#         UpdateExpression=update_expr,
#         ExpressionAttributeNames=attr_names,
#         ExpressionAttributeValues=expr_values,
#     )
