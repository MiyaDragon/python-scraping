from datetime import datetime

class ErrorMessage:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def ELEMENT_NOT_FOUND(self):
        return f"{self._timestamp()} [ERROR] 要素が見つからないため、処理が終了しました。"

    @property
    def ELEMENT_NOT_FOUND_OR_TIMEOUT(self):
        return f"{self._timestamp()} [ERROR] 要素が見つからないか、タイムアウトしました。"

    @property
    def SLACK_NOTIFY_FAILED(self):
        return f"{self._timestamp()} [ERROR] Slack通知に失敗しました。"

    @property
    def INVALID_ATTRIBUTE(self):
        return f"{self._timestamp()} [ERROR] 第一引数に誤った値が設定されています。"

    @staticmethod
    def with_detail(message: str, detail: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} {message} 詳細: {detail}"
