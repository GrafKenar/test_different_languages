from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_presence(browser):
    browser.get(link)
    basket_button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
    assert basket_button is not None, "there is no such button"
