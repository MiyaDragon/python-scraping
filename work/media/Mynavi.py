from media.Media import Media
from selenium.webdriver.common.by import By
import sys
import time
import driver
import const
from login.MediaLogin import MediaLogin
from common.CommonSelenium import CommonSelenium

class Mynavi(Media):
    """ 求人媒体「マイナビ転職」に関するクラス """

    media_name = const.MYNAVI_MEDIA_NAME

    login_info = {
        'login_url': const.MYNAVI_LOGIN_URL,
        'login_id_attr': {
            'attr': 'name',
            'attr_value': 'ap_login_id'
            },
        'login_pw_attr': {
            'attr': 'name',
            'attr_value': 'ap_password'
            },
        'login_id': const.MYNAVI_LOGIN_ID,
        'login_pw': const.MYNAVI_LOGIN_PW,
        'login_btn_attr': {
            'attr': 'id',
            'attr_value': 'loginBtn'
            },
    }
    
    # ログイン
    def login(self) -> None:
        # ログイン処理
        media_login = MediaLogin(self.driver)
        self.driver = media_login.login(self.login_info)
    
    # 応募者データ取得
    def get_applicant_data(self) -> dict:
        # 「応募管理」タブをクリック
        btn_element = self.driver.find_element(By.LINK_TEXT, '応募管理')
        CommonSelenium.target_click(self.driver, btn_element)
        time.sleep(5)

        # 新しいウィンドウにフォーカスを移動する
        handles = self.driver.window_handles
        new_window_handle = handles[-1]  # 最後に開かれたウィンドウのハンドルを取得
        # 新しいウィンドウに切り替える
        self.driver.switch_to.window(new_window_handle)

        # 応募者一覧を取得
        applicant_elements = CommonSelenium.get_elements('em', '書類選考', self.driver)
        # print(len(applicant_elements))
        # time.sleep(100)
        # applicant_elements = CommonSelenium.get_elements_by_attr('tag', 'article', self.driver)

        applicant_data = {}

        # 応募者が存在する場合
        if applicant_elements:
            for index, applicant_element in enumerate(applicant_elements):
                # if (index == 3):
                #     break
                # 「応募者」をクリック
                CommonSelenium.target_click(self.driver, applicant_element)
                time.sleep(5)

                ## 新しいウィンドウにフォーカスを移動する
                handles = self.driver.window_handles
                # 最後に開かれたウィンドウのハンドルを取得
                new_window_handle = handles[-1]
                # 新しいウィンドウに切り替える
                self.driver.switch_to.window(new_window_handle)

                # 応募者情報を取得
                applicant_info = self.get_applicant_info()
                # 応募者情報を辞書に格納
                applicant_data[index] = applicant_info

                # ウィンドウを閉じる
                self.driver.close()
                # 元のウィンドウに戻る
                self.driver.switch_to.window(handles[1])

                time.sleep(3)
        else:
            print('応募者は存在しません。')
            self.logout()
            sys.exit()
        
        return applicant_data
    
    # 応募者情報取得
    def get_applicant_info(self) -> dict:
        
        applicant_data = {}
        entry_history_data = {}

        ## 名前
        name_element = CommonSelenium.get_element_by_attr('xpath', '//*[@id="scrollContainer"]/main/div/div/main/header[1]/div[1]/h1/div/a', self.driver)
        applicant_data['last_name'] = CommonSelenium.get_text_split_single_unit(name_element.text, None, 0)
        applicant_data['first_name'] = CommonSelenium.get_text_split_single_unit(name_element.text, None, 1)
        ## 名前（カナ）
        kana_name_element = CommonSelenium.get_element_by_attr('xpath', '//*[@id="scrollContainer"]/main/div/div/main/header[1]/div[1]/h1/div/i', self.driver)
        applicant_data['last_name_kana'] = CommonSelenium.get_text_split_single_unit(kana_name_element.text, None, 0)
        applicant_data['first_name_kana'] = CommonSelenium.get_text_split_single_unit(kana_name_element.text, None, 1)
        ## エントリー日
        entry_date_element = CommonSelenium.get_element_by_attr('xpath', '//*[@id="visibleContainer"]/div[1]/article[1]/label/div/time', self.driver)
        entry_date = entry_date_element.text.replace('：', ' ')
        applicant_data['entry_date'] = CommonSelenium.get_text_split_single_unit(entry_date, None, 1)
        ## メール
        email_element = CommonSelenium.get_element_by_attr('xpath', '//*[@id="profile_ss"]/div[2]/dl[2]/dd[3]', self.driver)
        applicant_data['email'] = email_element.text
        ## 電話番号
        phone_element = CommonSelenium.get_element_by_attr('xpath', '//*[@id="profile_ss"]/div[2]/dl[2]/dd[2]', self.driver)
        applicant_data['phone'] = phone_element.text
        ## 性別
        gender_element = CommonSelenium.get_element_by_attr('xpath', '//*[@id="scrollContainer"]/main/div/div/main/header[1]/div[1]/h1/i[1]', self.driver)
        applicant_data['gender'] = CommonSelenium.get_text_split_single_unit(gender_element.text, None, 1)
        ## 誕生日
        birth_day_element = CommonSelenium.get_element_by_attr('xpath', '//*[@id="profile_ss"]/div[2]/dl[1]/dd[3]', self.driver)
        applicant_data['birth_day'] = CommonSelenium.get_text_split_single_unit(birth_day_element.text, None, 0)
        ## 都道府県
        address_elenet = CommonSelenium.get_element_by_attr('xpath', '//*[@id="profile_ss"]/div[2]/dl[1]/dd[2]', self.driver)
        address = CommonSelenium.get_text_split_single_unit(address_elenet.text, '\n', 1)
        prefecture = CommonSelenium.get_prefecture(address)
        applicant_data['prefecture'] = prefecture
        ## 媒体名
        applicant_data['media_name'] = const.MYNAVI_MEDIA_NAME
        # applicant_data['media_name'] = None
        # entry_history_data['media_name'] = const.MYNAVI_MEDIA_NAME
        # applicant_data['entry_history'] = entry_history_data
        ## 在籍状況
        applicant_data['enrollment_status'] = '不明'

        time.sleep(3)

        return applicant_data
    
    # ログアウト
    def logout(self) -> None:
        # ログアウトを実行
        self.driver.get(const.MYNAVI_LOGOUT_URL)
