from common.CommonSelenium import CommonSelenium
from messages.SuccessMessage import SuccessMessage

class MediaLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self, login_info: dict):
        # ブラウザでログインページを開く
        self.driver.get(login_info['login_url'])

        # ログインフォームの要素を取得
        login_id_input = CommonSelenium.get_element_by_attr(login_info['login_id_attr']['attr'], login_info['login_id_attr']['attr_value'], self.driver)
        login_pw_input = CommonSelenium.get_element_by_attr(login_info['login_pw_attr']['attr'], login_info['login_pw_attr']['attr_value'], self.driver)

        # ログインIDとパスワードを入力
        login_id_input.send_keys(login_info['login_id'])
        login_pw_input.send_keys(login_info['login_pw'])

        # ログインボタンをクリック
        login_btn = CommonSelenium.get_element_by_attr(login_info['login_btn_attr']['attr'], login_info['login_btn_attr']['attr_value'], self.driver)
        login_btn.click()

        # ログイン成功メッセージを出力
        print(SuccessMessage.LOGIN_SUCCESS())

        return self.driver
