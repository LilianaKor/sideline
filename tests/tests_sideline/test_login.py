from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


SIGN_IN_BTN = ('xpath', "(//a[text()='Team Site Sign In'])[1]")


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(browser):
    browser.get('https://go.teamsideline.com/')
    #browser.find_element(By.XPATH,


