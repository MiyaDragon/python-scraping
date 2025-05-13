class SuccessMessage:
    LOGIN_SUCCESS = "[SUCCESS] ログインに成功しました。"
    LOGOUT_SUCCESS = "[SUCCESS] ログアウトに成功しました。"
    GET_APPLICANT_DATA_SUCCESS = "[SUCCESS] 応募者情報の取得が完了しました。"
    STORE_JOB_SEEKER_RECORD_SUCCESS = "[SUCCESS] 求職者情報の登録が完了しました。"
    SPREAD_SHEET_WRITE_SUCCESS = "[SUCCESS] スプレッドシートへの書き込みが完了しました。"
    SLACK_NOTIFIED = "[SUCCESS] Slackへの通知に成功しました。"

    @staticmethod
    def with_detail(message: str, detail: str):
        return f"{message} 詳細: {detail}"
