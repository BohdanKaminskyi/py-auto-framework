import selenium.webdriver as webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Component:
    def __init__(self, *_, required=True, **selector):
        assert len(selector) == 1

        by, selector = next(iter(selector.items()))
        self.by = by.replace('_', ' ')
        self.selector = selector

        setattr(self, 'required', required)

        self.obj = None
        self.driver: webdriver.remote.webdriver.WebDriver = None

    def __get__(self, instance, owner):
        if not self.driver:
            self.driver = instance.driver

        self.obj = self.driver.find_element(self.by, self.selector)

        return self

    def __getattr__(self, item):
        return getattr(self.obj, item)

    def available(self):
        return bool(self.obj)

    def wait_while_absent(self, timeout=5):
        (
            WebDriverWait(self.driver, timeout)
            .until(lambda _: self.available)
         )


class Button(Component):
    def click(self):
        self.obj.click()


class Label(Component):
    @property
    def value(self):
        return self.obj.get_attribute('value')


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




