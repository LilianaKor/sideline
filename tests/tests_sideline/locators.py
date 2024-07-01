#AUTH
from selenium.webdriver.common.by import By

EMAIL_FIELD = "//input[@id='ctl00_ContentUnit_EmailTextBox']"
PASSWORD_FIELD = "//input[@id='ctl00_ContentUnit_PasswordTextBox']"
SIGN_IN_BTN = (By.CSS_SELECTOR, "#ctl00_ContentUnit_OkButton")

#SIGN_IN_BTN = "(//a[text()='Team Site Sign In'])[1]"
#SIGN_IN_BTN = (By.CSS_SELECTOR, ".rbText")
#SIGN_IN_BTN = (By.XPATH, "*[@id='ctl00_ContentUnit_OkButton']")