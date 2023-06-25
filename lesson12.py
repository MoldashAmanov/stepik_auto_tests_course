from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    ac = browser.find_element(By.ID, "num1")
    a = ac.text
    bc = browser.find_element(By.ID, "num2")
    b = bc.text

    c = str(int(a) + int(b))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)

    button = browser.find_element(By. TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

