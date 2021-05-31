from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")

#div[id='draggable']
#//div[@id='droppable']

class DragAndDrop():

    def testingDragAndDrop(self):
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()

        pathIframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(pathIframe)

        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        action.drag_and_drop(fromElement, toElement)
        action.perform()

        time.sleep(5)

        print("Am terminat")


dragAndDrop = DragAndDrop()
dragAndDrop.testingDragAndDrop()
driver.quit()

