from src.driver import driver
import allure
import pytest
from time import sleep
from selenium.common import exceptions

from src.pages.login import LoginPage


@allure.description('Verification:: User can not login with invalid credentials')
@pytest.mark.parametrize('login,password',
                         [('hello@sdla', 'world'),
                          ('helsslo@sdla', 'worsssald'),
                          ('heaaaaallo@sdla', 'wossdrld')
])
def test_CID111(driver, login, password):
    with LoginPage(driver) as login_page:

        login_page.email.value = login
        login_page.password.value = password
        login_page.login_button.click()

        try:
            assert login_page.invalid_login_or_password_text.is_displayed()
        except exceptions.NoSuchElementException:
            pytest.fail('Message not displayed')


#
# @allure.description('Verification:: Error message is displayed if user enters invalid email')
# @pytest.mark.parametrize('login,password',
#                          [('hello@sdla', 'world'),
#                           ('admin@gmail.com', 'admin'),
#                           ('admin@hot.com', 'password')])
# def test_CID111(driver, login, password):
#     with LoginPage(driver) as login_page:
#         login_page.email.value = login
#         login_page.password.value = password
#
#     assert True