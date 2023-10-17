# content of test_50.py
# import socket
import pytest
import allure
import os

@allure.epic('epic')
@allure.feature('feature')
@allure.story('story')
# @allure.description("""Test description""")
@allure.description_html("""<h1>Html test description</h1>""")
@allure.title("title")
# @allure.issue("https://github.com/allure-framework/allure-python/issues/24")
@allure.testcase("http://localhost:9999")
@allure.link("http://localhost:9999", name="local", link_type="homepage")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag('manual', 'manual 2')

@allure.parent_suite("parent suite name")
@allure.suite("suite name")
@allure.sub_suite("sub suite name")

def test_exp():
    # allure.dynamic.title("It is renamed test")
    allure.dynamic.parameter("password", '123', excluded=True)
    # allure.dynamic.link("allure", name="QAMETA", link_type="docs")
    allure.dynamic.parameter("work-dir", os.getcwd(), excluded=True)
    # allure.dynamic.parameter("password", "qwerty", mode=allure.parameter_mode.MASKED)
    # allure.dynamic.parameter("hostname", socket.gethostname(), mode=allure.parameter_mode.HIDDEN)
    with allure.step("step 1"):
        allure.attach("Some content in plain text", name='some attachment name', attachment_type=allure.attachment_type.TEXT)
        with allure.step("parent step"):
            with allure.step("grand parent step"):
                pass
    with allure.step("step 2"):
         allure.attach("Some content in plain text", name='some attachment name', attachment_type=allure.attachment_type.TEXT)
def test_exp_fail():
    pytest.fail('FAIL !!!')
def test_exp_skiped():
    pytest.skip('SKIPED !!!')
def test_exp_warning():
    pytest.warns('WARNING !!!')

# @pytest.mark.unknown
def test_exp_unknown():
    pass
    


def test_username(my_username):
    test_username.__doc__ = "Verify username and password for: " + str(my_username)
