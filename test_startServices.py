from typing import Dict, Any

import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService


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
    global appium_servie
    appium_servie = AppiumService()
    appium_servie.start()
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=AppiumOptions().load_capabilities(cap))
    yield driver
    driver.quit
    appium_servie.stop()


@pytest.mark.usefixtures("appium_driver")
def test_demo(appium_driver):
    print("started service")