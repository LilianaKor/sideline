from selenium.webdriver.common.by import By
import time
from tests.tests_sideline.locators import EMAIL_FIELD, PASSWORD_FIELD, SIGN_IN_BTN
from tests.tests_sideline.data import EMAIL, PASSWORD, MAIN_PAGE
import allure
import pytest


@allure.story('Login Feature')
@allure.title('Auth with valid credential')
@allure.severity(allure.severity_level.CRITICAL)
def test_signin_form(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, EMAIL_FIELD).send_keys(EMAIL)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    cookies_btn = driver.find_element(By.XPATH, "//*[@id='btn-set']").click()
    driver.find_element(*SIGN_IN_BTN)
    time.sleep(4)
    assert driver.current_url == "https://teamsideline.com/Team/SignIn.aspx"
