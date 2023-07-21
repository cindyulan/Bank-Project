import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from locator import elem
from locator import url
from data import input
import baselogincustomer


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    def test_a_deposit_success(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.acNumber).click() #click button
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.valNumber).text
        self.assertIn(input.valNumber, response_data) 

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()