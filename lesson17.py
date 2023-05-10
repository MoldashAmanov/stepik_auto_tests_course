from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button_1 = browser.find_element(By.TAG_NAME, "button")
    button_1.click()

    x_text = browser.find_element(By.ID, "input_value")
    x = x_text.text
    y = calc(x)

    input_y = browser.find_element(By.NAME, "text")
    input_y.send_keys(y)

    button_2 = browser.find_element(By.ID, "solve")
    button_2.click()
        
finally:
    time.sleep(30)
    browser.quit()

