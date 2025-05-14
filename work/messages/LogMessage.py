from datetime import datetime

class LogMessage:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def START_PROCESSING(media: str):
        return f"{LogMessage._timestamp()} [INFO] {media}の処理を開始します。"

    @staticmethod
    def END_PROCESSING():
        return f"{LogMessage._timestamp()} [INFO] 処理が完了しました。"

    @staticmethod
    def ELEMENT_FOUND():
        return f"{LogMessage._timestamp()} [INFO] 要素を正常に取得しました。"

    @staticmethod
    def ELEMENT_CLICKED():
        return f"{LogMessage._timestamp()} [INFO] 要素をクリックしました。"

    @staticmethod
    def VALUE_SENT():
        return f"{LogMessage._timestamp()} [INFO] テキストを送信しました。"

    @staticmethod
    def NOT_APPLICANT():
        return f"{LogMessage._timestamp()} [INFO] 応募者が存在しません。"

    @staticmethod
    def with_detail(message: str, detail: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} {message} 詳細: {detail}"
