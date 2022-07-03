import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()  # full screen
    yield browser
    browser.quit()
