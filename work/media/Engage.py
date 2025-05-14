from media.Media import Media
from selenium.webdriver.common.by import By
import time
import const
from login.MediaLogin import MediaLogin
from common.CommonSelenium import CommonSelenium
from common.CommonFormat import CommonFormat
from messages.ErrorMessage import ErrorMessage
from messages.SuccessMessage import SuccessMessage
from notification.SlackNotification import SlackNotification

class Engage(Media):
    """ 求人媒体engageに関するクラス """

    media_name = const.ENGAGE_MEDIA_NAME

    login_info = {
        'login_url': const.ENGAGE_LOGIN_URL,
        'login_id_attr': {
            'attr': 'id',
            'attr_value': 'loginID'
            },
        'login_pw_attr': {
            'attr': 'id',
            'attr_value': 'password'
            },
        'login_id': const.ENGAGE_LOGIN_ID,
        'login_pw': const.ENGAGE_LOGIN_PW,
        'login_btn_attr': {
            'attr': 'id',
            'attr_value': 'login-button'
            },
    }
    
    # ログイン
    def login(self) -> None:
        # ログイン処理
        media_login = MediaLogin(self.driver)
        self.driver = media_login.login(self.login_info)

    # 応募者データ取得
    def get_applicant_data(self) -> dict:
        try:
            # 応募者データ
            applicant_data = {}
            
            # 応募者一覧（名前）の取得
            applicant_list = self.get_applicant_list()

            # 応募者が存在しない場合、早期return
            if len(applicant_list) == 0:
                return applicant_data
            
            # ブラウザで選考中ページを開く
            self.driver.get(const.ENGAGE_MANAGE_PROCESSING_URL)
            time.sleep(3)

            for index, name in enumerate(applicant_list):
                # 応募者名をクリック
                target_element = CommonSelenium.get_element('a', name, self.driver)
                CommonSelenium.target_click(self.driver, target_element)
                time.sleep(3)

                # 応募者情報を取得
                applicant_info = self.get_applicant_info()
                # 応募者情報を辞書に格納
                applicant_data[self.media_name + str(index)] = applicant_info

                # モーダルが表示されている場合削除
                self.close_modal('md_drawer--show')
                time.sleep(3)
            
            # 応募者情報取得成功メッセージを出力
            print(SuccessMessage.GET_APPLICANT_DATA_SUCCESS())
            return applicant_data
        except Exception as e:
            msg = ErrorMessage.with_detail(ErrorMessage.ELEMENT_NOT_FOUND(), e)
            # Slackにエラーメッセージを送信
            SlackNotification().send_message(msg, mention="<!channel>")
            # エラーメッセージを出力
            print(msg)
        finally:
            # ログアウト
            self.logout()
            # WebDriverを終了する
            self.driver.quit()
    
    # 応募者一覧（名前）の取得
    def get_applicant_list(self) -> list:
        # 応募者一覧
        applicant_list = []
        
        # ブラウザで候補者管理ページを開く
        self.driver.get(const.ENGAGE_MANAGE_URL)
        time.sleep(3)

        # モーダルが表示されている場合削除
        self.close_modal('md_modal--show')
        time.sleep(3)

        # 応募者リスト
        target_elements = CommonSelenium.get_elements_by_attr('id', 'js_applicantList', self.driver)
        applicant_elements = CommonSelenium.get_elements_by_attr('class', 'accountName', target_elements[0])

        # 応募者が存在しない場合、早期return
        if len(applicant_elements) == 0:
            return applicant_list

        for applicant_element in applicant_elements:
            # 「プロフィール確認」をクリック
            target_element = CommonSelenium.get_element_by_attr('tag', 'a', applicant_element)
            CommonSelenium.target_click(self.driver, target_element)
            time.sleep(3)

            # 応募者名の取得
            applicant_full_name = self.get_applicant_full_name()
            # 応募者名をリストに格納
            applicant_list.append(applicant_full_name)

            # 「選考へ進める」をクリック
            selection_element = CommonSelenium.get_element_by_xpath('a', 'data-modal_action', 'applicantOk', self.driver)
            CommonSelenium.target_click(self.driver, selection_element)
            time.sleep(3)

            # モーダルが表示されている場合削除
            self.close_modal('md_modal--show')
            time.sleep(3)

        return applicant_list

    # 応募者情報の取得
    def get_applicant_info(self) -> dict:

        applicant_data = {}

        ## 名前
        name_element = CommonSelenium.get_element_by_xpath('div', 'class', 'name', self.driver)
        applicant_data['last_name'] = CommonSelenium.get_text_split_single_unit(name_element.text, None, 0)
        applicant_data['first_name'] = CommonSelenium.get_text_split_single_unit(name_element.text, None, 1)
        ## 名前（カナ）
        kana_name_element = CommonSelenium.get_element_by_xpath('div', 'class', 'kana', self.driver)
        applicant_data['last_name_kana'] = CommonSelenium.get_text_split_single_unit(kana_name_element.text, None, 0)
        applicant_data['first_name_kana'] = CommonSelenium.get_text_split_single_unit(kana_name_element.text, None, 1)
        ## エントリー日
        entry_date_element = CommonSelenium.get_element_by_xpath('div', 'class', 'entryData', self.driver)
        entry_date = CommonSelenium.get_text_split_single_unit(entry_date_element.text, '\n', 0)
        formated_entry_date = CommonFormat.convert_to_datetime(entry_date[:-1], '%Y年%m月%d日')
        applicant_data['entry_date'] = formated_entry_date.strftime('%Y/%m/%d')
        ## 住所
        target_element = CommonSelenium.get_element('div', '現住所', self.driver)
        address_element = CommonSelenium.get_next_element(target_element)
        applicant_data['address'] = address_element.text
        ## 電話番号
        target_element = CommonSelenium.get_element('div', '電話番号', self.driver)
        phone_element = CommonSelenium.get_next_element(target_element)
        applicant_data['phone'] = phone_element.text
        ## メール
        target_element = CommonSelenium.get_element('div', 'メールアドレス', self.driver)
        email_element = CommonSelenium.get_next_element(target_element)
        applicant_data['email'] = email_element.text
        ## 性別
        private_date_element = CommonSelenium.get_element_by_xpath('span', 'class', 'dataSet', self.driver)
        applicant_data['gender'] = CommonSelenium.get_text_split_single_unit(private_date_element.text, None, 1)
        ## 誕生日
        target_elements = CommonSelenium.get_elements('div', '年齢', self.driver)
        if target_elements:
            birth_day_element = CommonSelenium.get_next_element(target_elements[0])
            formated_birth_day = CommonFormat.convert_to_datetime(birth_day_element.text[:-5], '%Y年%m月%d日')
        else:
            target_element = CommonSelenium.get_element('div', '生年月日', self.driver)
            birth_day_element = CommonSelenium.get_next_element(target_element)
            birth_day = birth_day_element.text[:4] + birth_day_element.text[10:]
            formated_birth_day = CommonFormat.convert_to_datetime(birth_day.replace(' ', ''), '%Y年%m月%d日')
        applicant_data['birth_day'] = formated_birth_day.strftime('%Y/%m/%d')
        ## 都道府県
        applicant_data['prefecture'] = CommonSelenium.get_text_split_single_unit(private_date_element.text, None, 2)
        ## 媒体名
        applicant_data['media_name'] = const.ENGAGE_MEDIA_NAME
        ## 在籍状況
        employment_elements = CommonSelenium.get_elements('div', '就業している', self.driver)
        applicant_data['enrollment_status'] = '在職' if len(employment_elements) > 0 else '離職'

        time.sleep(3)

        return applicant_data
    
    # ログアウト
    def logout(self) -> None:
        # ログアウトを実行
        self.driver.get(const.ENGAGE_LOGOUT_URL)
        # ログアウト成功メッセージを出力
        print(SuccessMessage.LOGOUT_SUCCESS())
    
    # モーダル削除
    def close_modal(self, target_class_name: str) -> None:
        while True:
            show_modal_elements = self.driver.find_elements(By.CLASS_NAME, target_class_name)
            if show_modal_elements:
                # モーダルを削除
                self.driver.execute_script(f"arguments[0].classList.remove('{target_class_name}');", show_modal_elements[0])
                time.sleep(3)
            else:
                break
    
    # 応募者名の取得
    def get_applicant_full_name(self) -> str:
        name_data_element = self.driver.find_element(By.TAG_NAME, 'ruby')
        last_name = CommonSelenium.get_text_split_single_unit(name_data_element.text, '\n', 0)
        first_name = CommonSelenium.get_text_split_single_unit(name_data_element.text, '\n', 2)
        return last_name + first_name
