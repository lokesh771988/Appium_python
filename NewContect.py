from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.google.android.contacts',
    'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create contact").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='First name']").send_keys("lokesh")

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']").send_keys("0987654234")

driver.find_element(by=AppiumBy.XPATH, value=" //android.widget.Button[@text='Save']").click()