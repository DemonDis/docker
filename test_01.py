from selenium import webdriver
from pytest_bdd import scenario, when
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options 
import time

options = Options()
# options.headless = True
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)

# driver = webdriver.Firefox(service=Service('./drivers/geckodriver'))
# driver = webdriver.Firefox()

@scenario('test.feature', 'посещаю фронт')
def test_посещаю_фронт():
    """посещаю фронт."""
    pass

@when('я ya.ru', target_fixture="calc")
def have_five():
    """я ya.ru."""
    driver.get("http://www.ya.ru")
    time.sleep(7)
    text_example = '!!!!!!'
    driver.quit()
    return text_example

@when('я смотрю на картику')
def add_three(calc):
    print("CONSOLE LOG CALC =", calc)
    pass