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

    def test_a_transaction_success(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login1(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.transBtn).click() #click button
        time.sleep(3)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.transUrl)

    def test_b_buttonback(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login1(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.transBtn).click() #click button
        time.sleep(3)
        driver.find_element(By.XPATH, elem.bckBtn).click() #click button
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboarUrl)

    def test_c_butonreset(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login1(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.transBtn).click() #click button
        time.sleep(3)
        driver.find_element(By.XPATH, elem.rstBtn).click() #click button
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.transUrl) # type: ignore  
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()