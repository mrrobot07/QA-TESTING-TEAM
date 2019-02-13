from selenium import webdriver
from OrangeWebsite.Pages.loginPage import LoginPage
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.clic_loginButton()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()