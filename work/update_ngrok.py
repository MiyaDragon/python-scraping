# work/update_ngrok_url.py

import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import const

# NGROKのAPIでURLを取得（v3）
def get_ngrok_url():
    try:
        res = requests.get("http://ngrok:4040/api/tunnels")
        tunnels = res.json()['tunnels']
        for tunnel in tunnels:
            if tunnel['proto'] == 'https':
                return tunnel['public_url']
    except Exception as e:
        print("ngrokのURL取得エラー:", e)
    return None

# スプレッドシートに書き込む
def update_spreadsheet(ngrok_url):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    # 認証情報の読み込み
    credentials = ServiceAccountCredentials.from_json_keyfile_name("/work/credentials.json", scope)

    # 認証してクライアント作成
    client = gspread.authorize(credentials)

    # スプレッドシートを開く
    spreadsheet = client.open_by_key(const.SPREAD_SHEET_ENTRY_FORM_ID)

    # ワークシートの選択
    sheet = spreadsheet.worksheet(const.SPREAD_SHEET_ENTRY_FORM_WORKSHEET_NAME)
    print(ngrok_url)
    sheet.update(values=[[ngrok_url]], range_name='N1')
    print("スプレッドシート更新完了: ", ngrok_url)

if __name__ == "__main__":
    time.sleep(5)  # ngrokが立ち上がるまで少し待機
    url = get_ngrok_url()
    if url:
        update_spreadsheet(url)
    else:
        print("URL取得失敗")
