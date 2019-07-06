from pytest import fixture
import selenium.webdriver as webdrivers
from src.consts import REPORTS_PATH
import subprocess
# from functools import partial


@fixture(scope="session", params=['chrome'])
def driver(request):
    web_driver = getattr(webdrivers, request.param.title())()
    web_driver.implicitly_wait(1)
    request.addfinalizer(web_driver.quit)

    return web_driver