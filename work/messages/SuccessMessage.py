from datetime import datetime

class SuccessMessage:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def LOGIN_SUCCESS(self):
        return f"{self._timestamp()} [SUCCESS] ログインに成功しました。"

    @property
    def LOGOUT_SUCCESS(self):
        return f"{self._timestamp()} [SUCCESS] ログアウトに成功しました。"

    @property
    def GET_APPLICANT_DATA_SUCCESS(self):
        return f"{self._timestamp()} [SUCCESS] 応募者情報の取得が完了しました。"

    @property
    def STORE_JOB_SEEKER_RECORD_SUCCESS(self):
        return f"{self._timestamp()} [SUCCESS] 求職者情報の登録が完了しました。"

    @property
    def SPREAD_SHEET_WRITE_SUCCESS(self):
        return f"{self._timestamp()} [SUCCESS] スプレッドシートへの書き込みが完了しました。"

    @property
    def SLACK_NOTIFIED(self):
        return f"{self._timestamp()} [SUCCESS] Slackへの通知に成功しました。"

    @staticmethod
    def with_detail(message: str, detail: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} {message} 詳細: {detail}"
