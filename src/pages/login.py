from src.components import Input, Button, Label
from src.page_obj import PageObjectBase
from selenium import webdriver


class LoginPage(PageObjectBase):
    url = 'https://www.phptravels.net/login'
    email = Input(name='username')
    password = Input(name='password')
    login_button = Button(class_name='loginbtn')
    invalid_login_or_password_text = Label(required=False,
                                           xpath='//div[contains(text(), "' +
                                                 'Invalid Email or Password' +
                                                 '")]')
