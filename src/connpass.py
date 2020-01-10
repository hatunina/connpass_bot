import datetime
import pandas as pd
import requests

import warnings
warnings.simplefilter('ignore')


class Connpass():
    def __init__(self, params):
        self.url = "https://connpass.com/api/v1/event/"
        self.params = params

    def get_events(self):
        return requests.get(self.url, params=self.params)

    def check_events(self, events):
        cols = [
            "title",
            "catch",
            "description",
            "event_url",
            "started_at",
            "ended_at",
            "limit",
            "address",
            "place",
            "accepted",
            "waiting",
            "updated_at"
        ]

        df = pd.DataFrame(events.json()["events"])[cols]

        # 東京開催
        df["is_tokyo"] = df["address"].map(lambda x: 1 if "東京" in x else 0)
        df = df[df["is_tokyo"] == 1]

        # 最終更新から2日以内
        df["updated_at"] = pd.to_datetime(df["updated_at"])
        df["updated_elapsed_day"] = (datetime.datetime.today() - df["updated_at"]).dt.days
        target_df = df.query("updated_elapsed_day==1 or updated_elapsed_day==2")

        target_df["started_at"] = pd.to_datetime(target_df["started_at"])
        target_df["ended_at"] = pd.to_datetime(target_df["ended_at"])

        target_df["start_month"] = target_df["started_at"].dt.month
        target_df["start_day"] = target_df["started_at"].dt.day
        target_df["start_hour"] = target_df["started_at"].dt.hour
        target_df["start_minutes"] = target_df["started_at"].dt.minute
        target_df["end_hour"] = target_df["ended_at"].dt.hour
        target_df["end_minutes"] = target_df["ended_at"].dt.minute

        return target_df
