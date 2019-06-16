import selenium.webdriver as webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Component:
    def __init__(self, **selector):
        by, selector = next(iter(selector.items()))

        self.by = by
        self.selector = selector
        self.obj = None
        self.driver: webdriver.remote.webdriver.WebDriver = None

    def __get__(self, instance, owner):
        if not self.driver:
            self.driver = instance.driver

        if not self.obj:
            self.obj = self.driver.find_element(self.by, self.selector)

        return self

    def __getattr__(self, item):
        return getattr(self.obj, item)

    @property
    def available(self):
        return bool(self.obj)

    def wait_while_absent(self, timeout=10):
        (
            WebDriverWait(self.driver, timeout)
            .until(lambda _: self.available)
         )


class Button(Component):
    def click(self):
        self.obj.click()


class Input(Component):
    @property
    def value(self):
        return self.obj.get_attribute('value')

    @value.setter
    def value(self, new_val):
        self.obj.send_keys(new_val)


class Link(Component):
    @property
    def href(self):
        return self.obj.get_attribute('href')

    @property
    def text(self):
        return self.obj.text




