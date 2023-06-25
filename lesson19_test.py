from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestBrowser(unittest.TestCase):

    def test_link_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("ivanpetrov@yandex.ru") 

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
     
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def test_link_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("ivanpetrov@yandex.ru") 

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
     
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()


