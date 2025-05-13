import requests
import const
from messages.ErrorMessage import ErrorMessage

class SlackNotification:
    def send_message(self, message: str, mention: str = None):
        # mentionが指定されていれば先頭に追加
        if mention:
            message = f"{mention} {message}"

        payload = {
            "text": message
        }
        try:
            response = requests.post(const.SLACK_WEBHOOK_URL, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(ErrorMessage.with_detail(ErrorMessage.SLACK_NOTIFY_FAILED, e))
