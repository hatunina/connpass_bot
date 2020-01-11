"""
slack botを使う場合のモジュール
https://api.slack.com/bot-users
"""

import requests


class SlackBots():
    def __init__(self, slack_params):
        self.token = slack_params["token"]
        self.channel = slack_params["channel"]

    def post(self, msg):
        params = {
            'token': self.token,
            'channel': self.channel,
            'text': msg
        }

        res = requests.post(url="https://slack.com/api/chat.postMessage", params=params)

        if res.status_code != 200:
            raise Exception
