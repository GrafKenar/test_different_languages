import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def browser():
    print("\nstart browser for test")
    options = Options()
    user_language = 'en'
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser")
    browser.quit()
