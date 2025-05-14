from datetime import datetime

class ErrorMessage:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def ELEMENT_NOT_FOUND():
        return f"{ErrorMessage._timestamp()} [ERROR] 要素が見つからないため、処理が終了しました。"

    @staticmethod
    def ELEMENT_NOT_FOUND_OR_TIMEOUT():
        return f"{ErrorMessage._timestamp()} [ERROR] 要素が見つからないか、タイムアウトしました。"

    @staticmethod
    def SLACK_NOTIFY_FAILED():
        return f"{ErrorMessage._timestamp()} [ERROR] Slack通知に失敗しました。"

    @staticmethod
    def INVALID_ATTRIBUTE():
        return f"{ErrorMessage._timestamp()} [ERROR] 第一引数に誤った値が設定されています。"

    @staticmethod
    def with_detail(message: str, detail: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} {message} 詳細: {detail}"
