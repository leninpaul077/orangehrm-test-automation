from selenium.webdriver.common.by import By
from PageObjectModel.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    DASHBOARD = (By.XPATH, "//h6[text()='Dashboard']")

    def load(self):
        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        self.wait.until(lambda d: d.find_element(*self.DASHBOARD))
