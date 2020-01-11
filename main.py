from src.connpass import Connpass
from src.slack_bots import SlackBots
import src.util


def main():
    config_path = 'config.yaml'
    config = util.read_yaml(config_path)

    cnp = Connpass(config["params"])
    events = cnp.get_events()
    events_df = cnp.check_events(events)

    slack = SlackBots(config["slack"])
    for idx in range(len(events_df)):
        msg = \
            "```" \
            "{}\n" \
            "キャッチ: {}\n" \
            "URL: {}\n" \
            "開催日: {}月{}日\n" \
            "時間: {}時{}分 ~ {}時{}分\n" \
            "参加人数: 最大{}人 申込{}人 補欠{}人\n" \
            "場所: {} ({})"\
            "```" \
            .format(events_df.title.values[idx],
                    events_df.catch.values[idx],
                    events_df.event_url.values[idx],
                    events_df.start_month.values[idx],
                    events_df.start_day.values[idx],
                    events_df.start_hour.values[idx],
                    events_df.start_minutes.values[idx],
                    events_df.end_hour.values[idx],
                    events_df.end_minutes.values[idx],
                    events_df.limit.values[idx],
                    events_df.accepted.values[idx],
                    events_df.waiting.values[idx],
                    events_df.address.values[idx],
                    events_df.place.values[idx]
                    )

        slack.post(msg)


if __name__ == '__main__':
    main()