from selenium.webdriver.common.by import By
from PageObjectModel.base_page import BasePage


class LeavePage(BasePage):

    def add_leave_type(self, leave_type_name):

        self.click((By.LINK_TEXT, "Leave"))
        self.click((By.XPATH, "//span[contains(text(),'Configure')]"))
        self.click((By.LINK_TEXT, "Leave Types"))
        self.click((By.XPATH, "//button[normalize-space()='Add']"))

        self.type(
            (By.XPATH, "//label[text()='Name']/../following-sibling::div/input"),
            leave_type_name
        )

        self.click((By.XPATH, "//button[normalize-space()='Save']"))

    def assign_leave(self, leave_type_name):

        self.click((By.LINK_TEXT, "Assign Leave"))

        self.select_dynamic_dropdown(
            "//input[@placeholder='Type for hints...']",
            "a"
        )

        self.select_static_dropdown(
            "//label[text()='Leave Type']/../following-sibling::div//div[contains(@class,'select-text')]",
            leave_type_name
        )

        self.enter_date(
            "//label[text()='From Date']/../following-sibling::div//input",
            "2026-02-24"
        )

        self.enter_date(
            "//label[text()='To Date']/../following-sibling::div//input",
            "2026-02-25"
        )

        self.click((By.XPATH, "//button[normalize-space()='Assign']"))

        try:
            self.click((By.XPATH, "//button[normalize-space()='Ok']"))
        except:
            pass
