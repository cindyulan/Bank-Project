import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from locator import url
import baselogincustomer


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
      
    def test_a_login_success(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboarUrl) # type: ignore

    def test_b_login_success(self):
        # steps
        driver = self.browser #buka web browser
        baselogincustomer.positive_login1(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboarUrl) # type: ignore
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()