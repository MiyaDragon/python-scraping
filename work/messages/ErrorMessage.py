class ErrorMessage:
    ELEMENT_NOT_FOUND = "[ERROR] 要素が見つからないため、処理が終了しました。"
    ELEMENT_NOT_FOUND_OR_TIMEOUT = "[ERROR] 要素が見つからないか、タイムアウトしました。"
    SLACK_NOTIFY_FAILED = "[ERROR] Slack通知に失敗しました。"
    INVALID_ATTRIBUTE = "[ERROR] 第一引数に誤った値が設定されています。"
    
    @staticmethod
    def with_detail(message: str, detail: str):
        return f"{message} 詳細: {detail}"
