from salesforce.Salesforce import Salesforce
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.CommonSelenium import CommonSelenium
import time
import const

class SalesforceJobSeekerRecord(Salesforce):
    """ Salesforce 求職者レコードに関するクラス """

    # メイン処理
    def store(self, applicant_data: dict) -> None:
        try:
            for staff_data in applicant_data.values():
                # クライアントページへ遷移
                self.driver.get(const.SALESFORCE_JOB_SEEKER_MANAGE_URL)
                time.sleep(10)

                # 求職者レコード登録処理
                self.store_staff_data(staff_data)
        except Exception as e:
            print("要素が見つからないか、タイムアウトしました:", e)
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
        ## TODO: なぜか一番最後に入力したtextboxの値が消えるため、空文字を入力している
        self.input_text('PersonMobilePhone', '')
        # 保存ボタンクリック
        save_btn = self.driver.find_element(By.XPATH, "//button[@name='SaveEdit']")
        CommonSelenium.target_click(self.driver, save_btn)
        time.sleep(5)

    # テキストボックスに値を入力
    def input_text(self, name_attr: str, input_data: str) -> None:
        input_element = self.driver.find_element(By.XPATH, f"//input[@name='{name_attr}']")
        input_element.send_keys(input_data)
        time.sleep(2)
