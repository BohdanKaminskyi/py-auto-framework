import selenium.webdriver as webdriver
from src.components import Component, Button, Input
# from allure import
from time import sleep


class PageObjectMeta(type):
    def __new__(cls, name, bases, dct):
        page = super().__new__(cls, name, bases, dct)
        components = {}

        for key, val in dct.items():
            print(key, val)
            print(dir(val))
            if isinstance(val, Component) and val.required:
                components[key] = val

        page.components = components

        return page


class PageObjectBase(metaclass=PageObjectMeta):
    def __init__(self, driver: webdriver.remote.webdriver.WebDriver):
        self.driver = driver

    def __enter__(self):
        """
         Wait until all elements will be present at page
         After that return page
        """
        self.driver.get(self.url)
        [component.wait_while_absent() for _, component in self.components.items()]

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
