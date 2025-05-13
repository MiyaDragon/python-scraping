class LogMessage:
    START_PROCESSING = "[INFO] 処理を開始します。"
    END_PROCESSING = "[INFO] 処理が完了しました。"
    ELEMENT_FOUND = "[INFO] 要素を正常に取得しました。"
    ELEMENT_CLICKED = "[INFO] 要素をクリックしました。"
    VALUE_SENT = "[INFO] テキストを送信しました。"
    NOT_APPLICANT = "[INFO] 応募者が存在しません。"

    @staticmethod
    def with_detail(message: str, detail: str):
        return f"{message} 詳細: {detail}"
