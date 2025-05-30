from dotenv import load_dotenv
import os

# .envファイルの読み込み
load_dotenv()

## セールスフォース
# システム名
SALESFORCE_SYSTEM_NAME = "salesforce"
# ログインURL
SALESFORCE_LOGIN_URL = os.getenv("SALESFORCE_LOGIN_URL")
# ログインID
SALESFORCE_LOGIN_ID = os.getenv("SALESFORCE_LOGIN_ID")
# ログインPW
SALESFORCE_LOGIN_PW = os.getenv("SALESFORCE_LOGIN_PW")
# 2段階認証 sercretKey
AUTHENTICATOR_SERCRET_KEY = os.getenv("AUTHENTICATOR_SERCRET_KEY")
# 求職者管理URL
SALESFORCE_JOB_SEEKER_MANAGE_URL = os.getenv("SALESFORCE_JOB_SEEKER_MANAGE_URL")
# ログアウトURL
SALESFORCE_LOGOUT_URL = os.getenv("SALESFORCE_LOGOUT_URL")

## engage
# ログインURL
ENGAGE_LOGIN_URL = os.getenv("ENGAGE_LOGIN_URL")
# ログインID
ENGAGE_LOGIN_ID = os.getenv("ENGAGE_LOGIN_ID")
# ログインPW
ENGAGE_LOGIN_PW = os.getenv("ENGAGE_LOGIN_PW")
# 候補者管理URL
ENGAGE_MANAGE_URL = os.getenv("ENGAGE_MANAGE_URL")
# 応募者年齢上限
ENGAGE_APPLICANT_AGE_LIMIT = os.getenv("ENGAGE_APPLICANT_AGE_LIMIT")
# 候補者管理 > 選考中URL
ENGAGE_MANAGE_PROCESSING_URL = os.getenv("ENGAGE_MANAGE_PROCESSING_URL")
# 媒体名
ENGAGE_MEDIA_NAME = "engage"
# ログアウトURL
ENGAGE_LOGOUT_URL = os.getenv("ENGAGE_LOGOUT_URL")

## マイナビ転職
# ログインURL
MYNAVI_LOGIN_URL = os.getenv("MYNAVI_LOGIN_URL")
# ログインID
MYNAVI_LOGIN_ID = os.getenv("MYNAVI_LOGIN_ID")
# ログインPW
MYNAVI_LOGIN_PW = os.getenv("MYNAVI_LOGIN_PW")
# ログアウトURL
MYNAVI_LOGOUT_URL = os.getenv("MYNAVI_LOGOUT_URL")
# 媒体名
MYNAVI_MEDIA_NAME = "マイナビ"

## スプレッドシート
# スプレッドシート：KPI管理表
# ステータス
SPREAD_SHEET_KPI_DEFAULT_STATUS = "01_応募済み"
# ID
SPREAD_SHEET_KPI_ID = os.getenv("SPREAD_SHEET_KPI_ID")
# ワークシート名
SPREAD_SHEET_KPI_WORKSHEET_NAME = "【採用】候補者管理"
# 選考基準：年齢
SPREAD_SHEET_KPI_AGE_LIMIT = os.getenv("SPREAD_SHEET_KPI_AGE_LIMIT")
# スプレッドシート：エントリーフォーム
# ID
SPREAD_SHEET_ENTRY_FORM_ID = os.getenv("SPREAD_SHEET_ENTRY_FORM_ID")
# ワークシート名
SPREAD_SHEET_ENTRY_FORM_WORKSHEET_NAME = "フォームの回答 1"

## Slack
# Slack Webhook URL
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
