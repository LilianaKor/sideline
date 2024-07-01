from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_text_and_email(browser):
    browser.get('https://go.teamsideline.com/')
    link = browser.find_element(By.XPATH, '//a[text()="Text, Email, Chat Communications Notifications & More"]')
    link.click()
    header = browser.find_element(By.XPATH, '//h1[@class="page-header"]/span[text()="Text and Email Communications"]')
    assert header.is_displayed(), "Header 'Text and Email Communications' is not visible"



#
# def test_text_and_email():
#     browser = webdriver.Chrome()
#     browser.get('https://go.teamsideline.com/')
#     browser.find_element('xpath', '//a[text()="Text, Email, Chat Communications Notifications & More"]').click()
#     assert browser.title(By.XPATH, '//h1[@class="page-header"]/span[text()="Text and Email Communications"]').is visible