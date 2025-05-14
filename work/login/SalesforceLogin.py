from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from messages.SuccessMessage import SuccessMessage
import time
import pyotp

class SalesforceLogin:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, login_info: dict):
        # ブラウザでログインページを開く
        self.driver.get(login_info['login_url'])

        time.sleep(3)

        # ログインフォームの要素を取得
        login_id_input = self.driver.find_element(By.ID, login_info['login_id_attr'])
        login_pw_input = self.driver.find_element(By.ID, login_info['login_pw_attr'])

        # ログインIDとパスワードを入力
        login_id_input.send_keys(login_info['login_id'])
        login_pw_input.send_keys(login_info['login_pw'])

        # ログインボタンをクリック
        login_btn = self.driver.find_element(By.ID, login_info['login_btn_attr'])
        login_btn.click()

        time.sleep(3)

        # ワンタイムパスワードの生成
        totp_elemet = self.driver.find_element(By.ID, login_info['totp_attr'])
        totp = pyotp.TOTP(login_info['authenticator_sercret_key'])

        # ワンタイムパスワードを入力（Enterで決定）
        totp_elemet.send_keys(totp.now())
        totp_elemet.send_keys(Keys.ENTER)

        # ログインが成功するまで待機
        time.sleep(5)

        # ログイン成功メッセージを出力
        print(SuccessMessage.LOGIN_SUCCESS())

        return self.driver
