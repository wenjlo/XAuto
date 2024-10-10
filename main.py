from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from config import USERNAMES,PASSWORDS,TEXT_PATH
import time
from x_utils.tools import login,login_email_confirm,post

ua = UserAgent(os='windows',browsers='chrome')
userAgent = ua.chrome
print(userAgent)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options)

if __name__ == '__main__':
    driver.get('https://x.com/i/flow/login')

    for u,p in zip(USERNAMES,PASSWORDS):
        try:
            driver = login(driver,u,p)
        except:
            login_email_confirm(driver,u,p)
        post(driver,TEXT_PATH)
        time.sleep(1)
