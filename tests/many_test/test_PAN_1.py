import pytest
import allure
from fn_for.all_fn import fn_for_pytest

@allure.epic('epic_1')
@allure.feature('feature_1')
@allure.story('story_1')
@allure.title("title")

def test_exp_fail():
    fn_for_pytest
    pytest.fail('FAIL !!!')

@allure.epic('epic_2')
@allure.feature('feature_2')
@allure.story('story_2')
@allure.title("title")

def tests_exp_warning():
    fn_for_pytest
    pytest.warns('WARNING !!!')

@allure.epic('epic_2')
@allure.feature('feature_2')
@allure.story('story_2')
@allure.title("title")

def tests_exp_good():
    fn_for_pytest
