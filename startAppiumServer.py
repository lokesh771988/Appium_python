import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.hmh.api',
    'appActivity': '.ApiDemos',
    'language': 'en',
    'locale': 'US'
}

appium_server = AppiumService()
appium_server.start()

driver = webdriver.Remote('http://127.0.0.1:4444', options=AppiumOptions().load_capabilities(cap))


el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Chrome"]')
el.click()
driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText").send_keys("Lokesh")

appium_server.stop()