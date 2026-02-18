from selenium.webdriver.common.by import By
from PageObjectModel.base_page import BasePage


class RecruitmentPage(BasePage):

    def add_vacancy(self):

        self.click((By.XPATH, "//span[normalize-space()='Recruitment']"))
        self.click((By.LINK_TEXT, "Vacancies"))
        self.click((By.XPATH, "//button[normalize-space()='Add']"))

        self.type(
            (By.XPATH, "//label[text()='Vacancy Name']/../following-sibling::div/input"),
            "wer6"
        )

        self.select_static_dropdown(
            "//label[text()='Job Title']/../following-sibling::div//div[contains(@class,'select-text')]"
        )

        self.type(
            (By.XPATH, "//textarea[@placeholder='Type description here']"),
            "vgf"
        )

        self.select_dynamic_dropdown(
            "//input[@placeholder='Type for hints...']",
            "a"
        )

        self.type(
            (By.XPATH, "//label[text()='Number of Positions']/../following-sibling::div/input"),
            "1"
        )

        self.click((By.XPATH, "//button[normalize-space()='Save']"))

    def logout(self):
        self.click((By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"))
        self.click((By.XPATH, "//a[normalize-space()='Logout']"))
