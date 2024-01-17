import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    # return driver  # value will be stored permantly, extra variable


def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert "Login - VWO" == driver.title
