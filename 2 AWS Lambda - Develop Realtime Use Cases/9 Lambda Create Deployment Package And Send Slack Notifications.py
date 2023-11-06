import os
import json
import requests

slack_web_hook = os.environ('SLACK_WEBHOOK')

def send_slack(event, context):
    print(str(event))
    slack_message = {'text': 'EC2 Instance Stopped'}
    resp = requests.post(slack_web_hook, data=json.dumps(slack_message))
    return resp