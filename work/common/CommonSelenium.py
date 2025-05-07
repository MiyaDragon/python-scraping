from selenium.webdriver.common.by import By

class CommonSelenium:

    @staticmethod
    def get_element(tag_name: str, text_name: str, driver):
        # XPathを使用して特定のタグかつ特定のテキストを含む要素を取得する
        xpath_expression = f"//{tag_name}[contains(text(), '{text_name}')]"
        element = driver.find_element(By.XPATH, xpath_expression)
        return element

    @staticmethod
    def get_elements(tag_name: str, text_name: str, driver):
        # XPathを使用して特定のタグかつ特定のテキストを含む要素を取得する
        xpath_expression = f"//{tag_name}[contains(text(), '{text_name}')]"
        elements = driver.find_elements(By.XPATH, xpath_expression)
        return elements
    
    @staticmethod
    def get_element_by_attr(attr: str, attr_value: str, driver):
        match attr:
            case 'id':
                return driver.find_element(By.ID, attr_value)
            case 'class':
                return driver.find_element(By.CLASS_NAME, attr_value)
            case 'name':
                return driver.find_element(By.NAME, attr_value)
            case 'tag':
                return driver.find_element(By.TAG_NAME, attr_value)
            case 'xpath':
                return driver.find_element(By.XPATH, attr_value)
            case _:
                return print('第一引数に誤った値が設定されています。')
    
    @staticmethod
    def get_elements_by_attr(attr: str, attr_value: str, driver):
        match attr:
            case 'id':
                return driver.find_elements(By.ID, attr_value)
            case 'class':
                return driver.find_elements(By.CLASS_NAME, attr_value)
            case 'name':
                return driver.find_elements(By.NAME, attr_value)
            case 'tag':
                return driver.find_elements(By.TAG_NAME, attr_value)
            case 'xpath':
                return driver.find_elements(By.XPATH, attr_value)
            case _:
                return print('第一引数に誤った値が設定されています。')

    @staticmethod
    def get_element_by_xpath(tag: str, attr: str, attr_value: str, driver):
        return driver.find_element(By.XPATH, f"//{tag}[@{attr}='{attr_value}']")
    
    @staticmethod
    def get_elements_by_xpath(tag: str, attr: str, attr_value: str, driver):
        return driver.find_elements(By.XPATH, f"//{tag}[@{attr}='{attr_value}']")
    
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
        splited_text = text.split(delimiter)
        return splited_text[index]
    
    @staticmethod
    def get_prefecture(address: str):
        prefecture_list = ['都', '道', '府', '県']

        result = address

        for prefecture in prefecture_list:
            # 住所内にprefectureが存在しない場合はスキップ
            if prefecture not in address:
                continue

            # 特定の文字が最初に現れるインデックスを取得
            index = address.index(prefecture)
            if index > 1:
                result = address[:index+1]
                break
        
        return result
