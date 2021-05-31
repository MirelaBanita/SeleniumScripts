from selenium import webdriver
import time
from selenium.webdriver.common import by
driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")

class Facebook():

    def login(self):

        driver.get("https://facebook.com")
        acceptAll = driver.find_element_by_xpath("//button[contains(text(),'Acceptă tot')]")
        acceptAll.click()

        email = driver.find_element_by_xpath("//input[@id='email']")
        email.send_keys("email@yahoo.com")

        password = driver.find_element_by_xpath("//input[@id='pass']")
        password.send_keys("parola")

        Login = driver.find_element_by_xpath("//button[contains(text(),'Conectează-te')]")
        Login.click()

        time.sleep(10)

fb = Facebook()
fb.login()
