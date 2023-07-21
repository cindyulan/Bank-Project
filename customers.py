import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from locator import elem
from locator import url


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    
    def test_a_customers_success(self):
        driver = self.browser #buka web browser
        driver.get(url.baseUrl) #buka website
        time.sleep(1)
        driver.find_element(By.XPATH, elem.mngBtn).click() #click button
        time.sleep(1)
        driver.find_element(By.XPATH, elem.custsBtn).click() #click button
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.clistUrl) # type: ignore  

    def test_b_deletecustomers_success(self):
        driver = self.browser #buka web browser
        driver.get(url.baseUrl) #buka website
        time.sleep(1)
        driver.find_element(By.XPATH, elem.mngBtn).click() #click button
        time.sleep(1)
        driver.find_element(By.XPATH, elem.custsBtn).click() #click button
        time.sleep(1)
        driver.find_element(By.XPATH, elem.delBtn).click() #click button
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.clistUrl) # type: ignore  

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()