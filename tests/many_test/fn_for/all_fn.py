import pytest
import allure
import os

def fn_for_pytest():
    allure.dynamic.parameter("password", '123', excluded=True)
    allure.dynamic.parameter("work-dir", os.getcwd(), excluded=True)
    with allure.step("step 1"):
        allure.attach("Some content in plain text", name='some attachment name', attachment_type=allure.attachment_type.TEXT)
        with allure.step("parent step"):
            with allure.step("grand parent step"):
                pass
    with allure.step("step 2"):
         allure.attach("Some content in plain text", name='some attachment name', attachment_type=allure.attachment_type.TEXT)
