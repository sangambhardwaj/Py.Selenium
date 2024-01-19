import time

from selenium import webdriver
def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    print(driver.title)


    driver.back()
    driver.get("https://www.youtube.com")
    print(driver.title)

    driver.forward()
    print(driver.title)
    driver.refresh()
    driver.back()
    driver.refresh()


    time.sleep(5)
    driver.quit()