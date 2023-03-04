import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption("--user_language", action='store', default=None,
                     help="Choose language: ru, en, es")

@pytest.fixture(scope="function")
def language_expected_result(request):
    user_language = request.config.getoption("user_language")
    if user_language == 'ru':
        expected_result = 'Добавить в корзину'
    elif user_language == 'en':
        expected_result = 'Add to basket'
    elif user_language == 'es':
        expected_result = 'Añadir al carrito'
    elif user_language == 'fr':
        expected_result = 'Ajouter au panier'
    else:
        raise pytest.UsageError("--language_name should be: ru, en, es")
    yield expected_result
    print(f"\n{user_language}: '{expected_result}'")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("user_language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test")
        options_chrome = Options()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = FirefoxOptions()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser")
    browser.quit()
