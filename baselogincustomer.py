import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from locator import elem
from locator import url
from selenium.webdriver.support import expected_conditions as EC

def positive_login(driver):
    driver.get(url.baseUrl) #buka website
    time.sleep(3)
    driver.find_element(By.XPATH, elem.custBtn).click()  #click login
    time.sleep(3)
    driver.find_element(By.XPATH, elem.clName).click()  #click login
    time.sleep(3)
    driver.find_element(By.XPATH, elem.loginBtn).click()  #click login
    time.sleep(3)

def positive_login1(driver): 
    driver.get(url.baseUrl) #buka website
    time.sleep(3)
    driver.find_element(By.XPATH, elem.custBtn).click()  #click login
    time.sleep(3)
    driver.find_element(By.XPATH, elem.clName1).click()  #click login
    time.sleep(3)
    driver.find_element(By.XPATH, elem.loginBtn).click()  #click login
    time.sleep(3)


    