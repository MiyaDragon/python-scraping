from abc import ABC, abstractmethod 
from selenium.webdriver.common.by import By
from messages.LogMessage import LogMessage
import driver

class Media(ABC):
    def __init__(self):
        print(LogMessage.START_PROCESSING(self.media_name))
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
