from salesforce.Salesforce import Salesforce
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.CommonSelenium import CommonSelenium
import time
import const
from messages.SuccessMessage import SuccessMessage
from messages.ErrorMessage import ErrorMessage
from notification.SlackNotification import SlackNotification

class SalesforceJobSeekerRecord(Salesforce):
    """ Salesforce 求職者レコードに関するクラス """

    # メイン処理
    def store(self, applicant_data: dict) -> None:
        try:
            for staff_data in applicant_data.values():
                # クライアントページへ遷移
                self.driver.get(const.SALESFORCE_JOB_SEEKER_MANAGE_URL)
                time.sleep(5)

                # 求職者レコード登録処理
                self.store_staff_data(staff_data)

                # 求職者レコード登録完了メッセージを出力
                print(SuccessMessage.STORE_JOB_SEEKER_RECORD_SUCCESS)
        except Exception as e:
            msg = ErrorMessage.with_detail(ErrorMessage.ELEMENT_NOT_FOUND_OR_TIMEOUT, e)
            # Slackにエラーメッセージを送信
            SlackNotification.send_message(msg, mention="<!channel>")
            # エラーメッセージを出力
            print(msg)
        finally:
            # ログアウト
            self.logout()
            # WebDriverを終了する
            self.driver.quit()
            
    # 求職者レコード登録
    def store_staff_data(self, staff_data) -> None:
        # 新規ボタンクリック
        create_btn = CommonSelenium.get_element_by_xpath('a', 'title', '新規', self.driver)
        CommonSelenium.target_click(self.driver, create_btn)
        time.sleep(5)

        # 求職者クリック
        target_element = CommonSelenium.get_element_by_attr('id', '012IR0000015XTqYAM', self.driver)
        CommonSelenium.target_click(self.driver, target_element)
        time.sleep(5)

        # 次へボタンクリック
        target_element = CommonSelenium.get_element('span', '次へ', self.driver)
        parent_element = target_element.find_element(By.XPATH, './..')
        CommonSelenium.target_click(self.driver, parent_element)
        time.sleep(5)

        ### フォーム要素を特定して値を入力する
        ## 名前
        # 姓
        if staff_data['last_name'] is not None:
            self.input_text('lastName', staff_data['last_name'])
        # 名
        if staff_data['first_name'] is not None:
            self.input_text('firstName', staff_data['first_name'])
        ## 氏名カナ（姓）
        if staff_data['last_name_kana'] is not None:
            self.input_text('Sai__c', staff_data['last_name_kana'])
        ## 氏名カナ（名）
        if staff_data['first_name_kana'] is not None:
            self.input_text('Mai__c', staff_data['first_name_kana'])
        ## 誕生日
        if staff_data['birth_day'] is not None:
            self.input_text('PersonBirthdate', staff_data['birth_day'])
        ## メール
        if staff_data['email'] is not None:
            self.input_text('PersonEmail', staff_data['email'])
        ## 電話番号
        if staff_data['phone'] is not None:
            self.input_text('PersonMobilePhone', staff_data['phone'])
        ## 性別
        if staff_data['gender'] is not None:
            gender_element = CommonSelenium.get_element('label', '性別', self.driver)
            gender_box_id_name = gender_element.get_attribute('for')
            target_element = CommonSelenium.get_element_by_xpath('button', 'id', gender_box_id_name, self.driver)
            time.sleep(5)
            CommonSelenium.target_click(self.driver, target_element)
            time.sleep(5)
            id_number = gender_box_id_name.split('-')[-1]
            gender_number = '1' if staff_data['gender'] == '男性' else '2'
            gender_id_name = f'{gender_box_id_name}-{gender_number}-{id_number}'
            gender_element = CommonSelenium.get_element_by_xpath('lightning-base-combobox-item', 'id', gender_id_name, self.driver)
            time.sleep(5)
            CommonSelenium.target_click(self.driver, gender_element)
            time.sleep(5)
        ## 住所
        if staff_data['address'] is not None:
            self.input_text('country', '日本')
            self.input_text('province', staff_data['prefecture'])
            after_prefecture = CommonSelenium.get_after_prefecture(staff_data['address'])
            self.input_text('city', after_prefecture)
        # 保存ボタンクリック
        save_btn = self.driver.find_element(By.XPATH, "//button[@name='SaveEdit']")
        CommonSelenium.target_click(self.driver, save_btn)
        time.sleep(5)

    # テキストボックスに値を入力
    def input_text(self, name_attr: str, input_data: str) -> None:
        input_element = self.driver.find_element(By.XPATH, f"//input[@name='{name_attr}']")
        input_element.send_keys(input_data)
        time.sleep(2)
