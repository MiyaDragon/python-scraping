from login.SalesforceLogin import SalesforceLogin
import const
import driver

class Salesforce:
    """ Salesforceに関するクラス """

    # ログイン情報
    login_info = {
        'login_url': const.SALESFORCE_LOGIN_URL,
        'login_id_attr': 'username',
        'login_pw_attr': 'password',
        'login_id': const.SALESFORCE_LOGIN_ID,
        'login_pw': const.SALESFORCE_LOGIN_PW,
        'login_btn_attr': 'Login',
        'totp_attr': 'tc',
        'authenticator_sercret_key': const.AUTHENTICATOR_SERCRET_KEY,
    }

    def __init__(self):
        print("Salesforceの処理を開始します。")
        self.driver = driver.getDriver()
        self.login()
        
    def login(self) -> None:
        salesforce_login = SalesforceLogin(self.driver)
        self.driver = salesforce_login.login(self.login_info)
    
    def logout(self) -> None:
        # ログアウトを実行
        self.driver.get(const.SALESFORCE_LOGOUT_URL)
