import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import allure
from datetime import datetime


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()


# class ChromeService:
#     pass
#
#
# @pytest.fixture(scope="function")
# def driver1():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     attach = driver.get_screenshot_as_png()
#     allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
