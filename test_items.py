from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languages(browser):
    browser.get(link)
    basket_button_text = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    assert basket_button_text is not None