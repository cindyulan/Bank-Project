import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from locator import elem
from locator import url
from data import input


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    
    def test_a_addcustomer_success(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(url.baseUrl) #buka website
        time.sleep(1)
        driver.find_element(By.XPATH, elem.mngBtn).click() #click button 
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button
        time.sleep(1)
        driver.find_element(By.XPATH, elem.inpFirst).send_keys(input.inpFirst) #input
        time.sleep(1)
        driver.find_element(By.XPATH, elem.inpLast).send_keys(input.inpLast) #input
        time.sleep(1)
        driver.find_element(By.XPATH, elem.inpPost).send_keys(input.inpPost) #input
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn1).click() #click button
        time.sleep(5)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.addUrl) # type: ignore  

    def test_b_addcustomer_invfailed(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(url.baseUrl) #buka website
        time.sleep(1)
        driver.find_element(By.XPATH, elem.mngBtn).click() #click button 
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button
        time.sleep(1)
        driver.find_element(By.XPATH, elem.inpFirst).send_keys(input.inpFirst) #input 
        time.sleep(1)
        driver.find_element(By.XPATH, elem.inpLast).send_keys(input.inpLast) #input 
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn1).click() #click button
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.addUrl) # type: ignore

    def test_c_addcustomer_blankfailed(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(url.baseUrl) #buka website
        time.sleep(1)
        driver.find_element(By.XPATH, elem.mngBtn).click() #click button 
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn1).click() #click button
        time.sleep(1)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.addUrl) # type: ignore

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()