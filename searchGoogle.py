import time

from selenium import webdriver

class ChromeDriver():

    def searchGoogle(self):
        driver = webdriver.Chrome(executable_path ="D:\\chromedriver\\chromedriver.exe")
        driver.get("https://google.com")


        element =driver.find_element_by_id("L2AGLb")
        element.click()

        element_search= driver.find_element_by_name("q")
        element_search.send_keys("selenium")
        element_search.submit()


        #name="q"

        time.sleep(30)

        #id="L2AGLb"
        #id="L2AGLb"


search = ChromeDriver()
search.searchGoogle()
