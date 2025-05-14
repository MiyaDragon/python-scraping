from datetime import datetime

class LogMessage:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def START_PROCESSING(media: str):
        return f"{LogMessage._timestamp()} [INFO] {media}の処理を開始します。"

    @property
    def END_PROCESSING(self):
        return f"{self._timestamp()} [INFO] 処理が完了しました。"

    @property
    def ELEMENT_FOUND(self):
        return f"{self._timestamp()} [INFO] 要素を正常に取得しました。"

    @property
    def ELEMENT_CLICKED(self):
        return f"{self._timestamp()} [INFO] 要素をクリックしました。"

    @property
    def VALUE_SENT(self):
        return f"{self._timestamp()} [INFO] テキストを送信しました。"

    @property
    def NOT_APPLICANT(self):
        return f"{self._timestamp()} [INFO] 応募者が存在しません。"

    @staticmethod
    def with_detail(message: str, detail: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} {message} 詳細: {detail}"
