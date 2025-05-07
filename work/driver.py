from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import const

def getDriver():
    # # WebDriverのオプション設定
    # options = Options()
    # # ヘッドレスモード（画面を表示しない）
    # options.add_argument('--headless')
    # options.add_argument("--no-sandbox")
    # # options.add_argument("--disable-dev-shm-usage")

    # # WebDriverのセッションを作成
    # # return webdriver.Chrome(service=Service(executable_path=const.WEBDRIVER_PATH), options=options)
    # return webdriver.Chrome(options=options)

    options = webdriver.ChromeOptions()
    return webdriver.Remote(
                command_executor = 'http://selenium:4444/wd/hub',
                options = options
                )
    
