from typing import Dict, Any

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': "uiautomator2",
        'deviceName': 'Android',
        'appPackage': 'com.hmh.api',
        'appActivity': '.ApiDemos',
        'language': 'en',
        'locale': 'US'
    }

    url = 'http://localhost:4724'
    global driver
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    yield driver
    driver.quit


@pytest.fixture()
def adding_screenshot_Fail(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="alert message1", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=['device1', 'device2'], scope="function")
def appium_driver1(request):
    global driver
    if request.param == "device1":
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': "uiautomator2",
            'udid': 'emulator-5554',
            'appPackage': 'com.hmh.api',
            'appActivity': '.ApiDemos',
            'language': 'en',
            'locale': 'US'
        }
        url = 'http://localhost:4724'
        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    if request.param == "device2":
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': "uiautomator2",
            'udid': 'emulator-5556',
            'appPackage': 'com.hmh.api',
            'appActivity': '.ApiDemos',
            'language': 'en',
            'locale': 'US'
        }
        url = 'http://localhost:4728'
        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    yield driver
    driver.quit