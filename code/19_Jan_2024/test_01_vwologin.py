# Open the browser
# Navigate to a URL
# Find the Email WebElement and email id = "abc@gmail.com"
# Find the password inputbox and enter the passward = 123
#  Click on the botton - sign in
import time

# Verify that the Dashboard is loaded - Pytest
# Create a Report to send to QA Lead - HTML --> Allure Report

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    # Open the browser
    # Navigate to a URL
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("__start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")

    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    email_address_ele = driver.find_element(By.ID,"login-username")
    password_ele = driver.find_element(By.NAME, "password")
    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")
    email_address_ele.send_keys("sangambhardwaj05@gmail.com")
    password_ele.send_keys("Sangam@5004")
    sign_in_button_ele.click()

    time.sleep(10)
    LOGGER.info("this is "+ driver.title)
    assert "Dashboard" in driver.title
