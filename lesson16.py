from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.TAG_NAME, "button")
    button_1.click()
  
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    
    x_text = browser.find_element(By.ID, "input_value")
    x = x_text.text
    y = calc(x)

    input_y = browser.find_element(By.NAME, "text")
    input_y.send_keys(y)

    button_2 = browser.find_element(By.TAG_NAME, "button")
    button_2.click()

finally:
    time.sleep(30)
    browser.quit()


