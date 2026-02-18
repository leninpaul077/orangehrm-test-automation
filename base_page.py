from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def select_dynamic_dropdown(self, input_xpath, search_text):
        input_box = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, input_xpath))
        )
        input_box.click()
        input_box.send_keys(search_text)

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']"))
        )

        first_option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//div[@role='listbox']//span)[1]")
            )
        )
        first_option.click()

    def select_static_dropdown(self, dropdown_xpath, option_text=None):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
        )
        dropdown.click()

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']"))
        )

        if option_text:
            option = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[@role='listbox']//span[text()='{option_text}']")
                )
            )
        else:
            option = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//div[@role='listbox']//span)[1]")
                )
            )

        option.click()

    def enter_date(self, field_xpath, date_value):
        date_field = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, field_xpath))
        )
        date_field.click()
        time.sleep(0.5)
        date_field.send_keys(Keys.CONTROL + "a")
        date_field.send_keys(Keys.DELETE)
        date_field.send_keys(date_value)
        date_field.send_keys(Keys.TAB)

    def get_toast_text(self):
        toast = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "oxd-toast-content-text")
            )
        )
        return toast.text
