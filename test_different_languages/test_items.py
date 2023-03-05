from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languages(browser, language_expected_result):
    browser.get(link)
    basket_button_text = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button').text
    assert basket_button_text == language_expected_result, f"actual result is {text} while expected result is {language_expected_result}"
