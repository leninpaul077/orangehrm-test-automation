from PageObjectModel.login_page import LoginPage
from PageObjectModel.leave_page import LeavePage
from PageObjectModel.recruitment_page import RecruitmentPage


def test_orangehrm_flow(driver):

    login = LoginPage(driver)
    leave = LeavePage(driver)
    recruitment = RecruitmentPage(driver)

    # LOGIN
    login.load()
    login.login("Admin", "admin123")

    # ADD LEAVE TYPE
    leave_type_name = "AutoLeaveType4532"
    leave.add_leave_type(leave_type_name)
    assert "Success" in leave.get_toast_text()

    # ASSIGN LEAVE
    leave.assign_leave(leave_type_name)
    assert "Warning" or "Success" in leave.get_toast_text()

    # ADD VACANCY
    recruitment.add_vacancy()

    # LOGOUT
    recruitment.logout()
