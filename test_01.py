from selenium import webdriver
from pytest_bdd import scenario, when
from selenium.webdriver.firefox.options import Options as FirefoxOptions
#object of FirefoxOptions
options = webdriver.FirefoxOptions()
#set options.headless to True
options.headless = True
driver = webdriver.Firefox(executable_path="./drivers/geckodriver", options=options)

@scenario('test_01.feature', 'посещаю фронт')
def test_посещаю_фронт():
    """посещаю фронт."""
    pass

@when('я ya.ru', target_fixture="calc")
def have_five():
    """я ya.ru."""
    driver.get("http://www.ya.ru")
    text_example = '!!!!!!'
    return text_example

@when('я смотрю на картику')
def add_three(calc):
    print("CONSOLE LOG CALC =", calc)