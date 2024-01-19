import time

from selenium import webdriver


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    print(driver.title)

    time.sleep(5)
    driver.refresh()

    # driver.close() # Close will close the current window(tab)
    # it will not close the othertab


    driver.quit()
    # session == None
    # Close all the tabs(windows)