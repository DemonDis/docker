from selenium import webdriver
from pytest_bdd import scenario, when
from selenium.webdriver.chrome.options import Options 
 
options = Options()
options.add_argument("headless")
options.add_argument("no-sandbox")
options.add_argument("disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

@scenario('test.feature', 'посещаю фронт')
def test_посещаю_фронт():
    """посещаю фронт."""
    pass

@when('я ya.ru', target_fixture="calc")
def have_five():
    """я ya.ru."""
    driver.get("http://www.ya.ru")
    text_example = '!!!!!!'
    driver.quit()
    return text_example

@when('я смотрю на картику')
def add_three(calc):
    print("CONSOLE LOG CALC =", calc)
    pass