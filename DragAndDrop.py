from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.mobeta.android.demodslv',
    'appActivity': '.Launcher',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]').click()

driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic usage playground"]').click()

element = driver.find_elements(AppiumBy.XPATH, '//android.widget.ImageView['
                                               '@resource-id="com.mobeta.android.demodslv:id/drag_handle"]')

actions = TouchAction(driver)

actions.press(element[0]).wait(3000).move_to(element[5]).perform().release()





