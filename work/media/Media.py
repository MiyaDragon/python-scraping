from abc import ABC, abstractmethod 
from selenium.webdriver.common.by import By
import driver

class Media(ABC):
    def __init__(self):
        print(f"{self.media_name}の処理を開始します。")
        self.driver = driver.getDriver()
        # 暗黙的な待機を設定
        self.driver.implicitly_wait(10)
        # ログイン処理
        self.login()
    
    
    @abstractmethod
    def get_applicant_data(self):
        pass

    @abstractmethod
    def get_applicant_info(self):
        pass
    
    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def logout(self):
        pass
