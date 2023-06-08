from splinter import Browser
from pytest_bdd import scenario, when
import time

browser = Browser('firefox')
# browser = Browser('chrome')

@scenario('test_01.feature', 'посещаю фронт')
def test_посещаю_фронт():
    """посещаю фронт."""
    pass

@when('я ya.ru', target_fixture="calc")
def have_five():
    """я ya.ru."""
    browser.visit("http://www.ya.ru")
    browser.find_by_css('input[class="search3__input mini-suggest__input"]').fill('TEXT EXAMPLE')
    text_example = browser.find_by_css('span[class="a11y-hidden"]').text
    time.sleep(3) #sleep for 3 sec
    browser.screenshot()
    browser.quit()
    return text_example

@when('я смотрю на картику')
def add_three(calc):
    print("CONSOLE LOG CALC =", calc)
   