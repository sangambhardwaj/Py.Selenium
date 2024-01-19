import time

from selenium import webdriver
import logging

def test_open_login():
    driver = webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com")
    # driver.post("https//localhost:9515/session")
    driver.maximize_window()
    time.sleep(5)
    LOGGER.info(driver.title)
    # time.sleep(200)
    driver.quit()
    #session == None
    #Close all the tabs(windows)