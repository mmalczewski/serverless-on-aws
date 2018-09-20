import json
import os


def handle(event, context):
    body = {
        "message": "Serverless AWS demo, project name: %s, stage: %s" % (
            os.environ['PROJECT_NAME'], os.environ['STAGE_NAME']),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
