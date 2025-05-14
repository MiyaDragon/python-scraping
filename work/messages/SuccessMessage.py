from datetime import datetime

class SuccessMessage:
    @staticmethod
    def _timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def LOGIN_SUCCESS():
        return f"{SuccessMessage._timestamp()} [SUCCESS] ログインに成功しました。"

    @staticmethod
    def LOGOUT_SUCCESS():
        return f"{SuccessMessage._timestamp()} [SUCCESS] ログアウトに成功しました。"

    @staticmethod
    def GET_APPLICANT_DATA_SUCCESS():
        return f"{SuccessMessage._timestamp()} [SUCCESS] 応募者情報の取得が完了しました。"

    @staticmethod
    def STORE_JOB_SEEKER_RECORD_SUCCESS():
        return f"{SuccessMessage._timestamp()} [SUCCESS] 求職者情報の登録が完了しました。"

    @staticmethod
    def SPREAD_SHEET_WRITE_SUCCESS():
        return f"{SuccessMessage._timestamp()} [SUCCESS] スプレッドシートへの書き込みが完了しました。"

    @staticmethod
    def SLACK_NOTIFIED():
        return f"{SuccessMessage._timestamp()} [SUCCESS] Slackへの通知に成功しました。"

    @staticmethod
    def with_detail(message: str, detail: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} {message} 詳細: {detail}"
