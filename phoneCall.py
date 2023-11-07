from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.google.android.dialer',
    'appActivity': 'com.android.dialer.main.impl.MainActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Recents']").click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="key pad").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='1']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='2']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='3']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='4']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='5']").click()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="dial").click()

