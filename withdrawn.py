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

    def test_a_withdrawn_success(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.wdrBtn).click() #click button
        time.sleep(3)
        driver.find_element(By.XPATH, elem.formWdr).send_keys(input.withdrawn) #input
        time.sleep(1)
        driver.find_element(By.XPATH, elem.swdrBtn).click() #click button
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.valWdr).text
        self.assertIn(input.valWdr, response_data)
    def test_b_withdrawn_invfailed(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.wdrBtn).click() #click button
        time.sleep(3)
        driver.find_element(By.XPATH, elem.formWdr).send_keys(input.withdrawn1) #input
        time.sleep(1)
        driver.find_element(By.XPATH, elem.swdrBtn).click() #click button
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.valWdr1).text
        self.assertIn(input.valWdr1, response_data)

    def test_c_withdrawn_blankfailed(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.wdrBtn).click() #click button 
        time.sleep(3)
        driver.find_element(By.XPATH, elem.swdrBtn).click() #click button
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboarUrl) # type: ignore  

    def test_d_withdrawn_inv2failed(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login(driver)
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.wdrBtn).click() #click button 
        time.sleep(1)
        driver.find_element(By.XPATH, elem.formWdr).send_keys(input.invWithdrawn) #input 
        time.sleep(1)
        driver.find_element(By.XPATH, elem.swdrBtn).click() #click button 
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboarUrl) # type: ignore  
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()