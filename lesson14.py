from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.NAME, "firstname")	
    input_1.send_keys("Ivan")

    input_2 = browser.find_element(By.NAME, "lastname")
    input_2.send_keys("Ivanov")

    input_3 = browser.find_element(By.NAME, "email")
    input_3.send_keys("ivanov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

    
