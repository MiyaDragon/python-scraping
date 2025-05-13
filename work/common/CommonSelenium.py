from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CommonSelenium:
    TIMEOUT = 30  # 最大待機時間（秒）

    @staticmethod
    def get_element(tag_name: str, text_name: str, driver):
        xpath = f"//{tag_name}[contains(text(), '{text_name}')]"
        try:
            return WebDriverWait(driver, CommonSelenium.TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            print(f"要素が見つかりません: {xpath}")
            return None

    @staticmethod
    def get_elements(tag_name: str, text_name: str, driver):
        xpath = f"//{tag_name}[contains(text(), '{text_name}')]"
        return driver.find_elements(By.XPATH, xpath)

    @staticmethod
    def get_element_by_attr(attr: str, attr_value: str, driver):
        by_map = {
            'id': By.ID,
            'class': By.CLASS_NAME,
            'name': By.NAME,
            'tag': By.TAG_NAME,
            'xpath': By.XPATH,
        }
        by = by_map.get(attr)
        if not by:
            print('第一引数に誤った値が設定されています。')
            return None
        try:
            return WebDriverWait(driver, CommonSelenium.TIMEOUT).until(
                EC.presence_of_element_located((by, attr_value))
            )
        except TimeoutException:
            print(f"要素が見つかりません: {attr}={attr_value}")
            return None

    @staticmethod
    def get_elements_by_attr(attr: str, attr_value: str, driver):
        by_map = {
            'id': By.ID,
            'class': By.CLASS_NAME,
            'name': By.NAME,
            'tag': By.TAG_NAME,
            'xpath': By.XPATH,
        }
        by = by_map.get(attr)
        if not by:
            print('第一引数に誤った値が設定されています。')
            return []
        return driver.find_elements(by, attr_value)

    @staticmethod
    def get_element_by_xpath(tag: str, attr: str, attr_value: str, driver):
        xpath = f"//{tag}[@{attr}='{attr_value}']"
        try:
            return WebDriverWait(driver, CommonSelenium.TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            print(f"要素が見つかりません: {xpath}")
            return None

    @staticmethod
    def get_elements_by_xpath(tag: str, attr: str, attr_value: str, driver):
        xpath = f"//{tag}[@{attr}='{attr_value}']"
        return driver.find_elements(By.XPATH, xpath)

    @staticmethod
    def get_next_element(target_element):
        return target_element.find_element(By.XPATH, './following-sibling::*')

    @staticmethod
    def get_prev_element(target_element):
        return target_element.find_element(By.XPATH, './preceding-sibling::*')

    @staticmethod
    def target_click(driver, target_element):
        driver.execute_script("arguments[0].click();", target_element)

    @staticmethod
    def get_text_split_single_unit(text, delimiter, index):
        return text.split(delimiter)[index]

    @staticmethod
    def get_prefecture(address: str):
        for suffix in ['都', '道', '府', '県']:
            if suffix in address:
                return address[:address.index(suffix)+1]
        return address
    
    @staticmethod
    def get_after_prefecture(address: str):
        for suffix in ['都', '道', '府', '県']:
            if suffix in address:
                return address[address.index(suffix)+1:]
        return address
