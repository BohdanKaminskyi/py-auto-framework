import selenium.webdriver as webdriver
from src.components import Component, Button, Input


class PageObjectMeta(type):
    def __new__(cls, name, bases, dct):
        page = super().__new__(cls, name, bases, dct)
        components = {}

        for key, val in dct.items():
            print(key, val)
            if isinstance(val, Component):
                components['key'] = val

        page.components = components

        return page


class PageObjectBase(metaclass=PageObjectMeta):
    def __init__(self, driver: webdriver.remote.webdriver.WebDriver):
        self.driver = ''

    def __enter__(self):
        [component.wait_while_absent() for _, component in self.components.items()]

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class GoogleSearchPage(PageObjectBase):
    # sign_in = Button(id='gb_70')
    # search_input = Input(name='q')
    name = Input(name='username')

