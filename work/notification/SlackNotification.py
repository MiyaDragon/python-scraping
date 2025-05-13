import requests

class SlackNotification:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_message(self, message: str):
        payload = {
            "text": message
        }
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Slack通知に失敗しました: {e}")
