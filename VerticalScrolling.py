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
    'appPackage': 'com.hmh.api',
    'appActivity': '.ApiDemos',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

if driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').is_displayed():
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()
    wait = WebDriverWait(driver, 10)
    el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
    el1.click()

wait1 = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
el2 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='App']")))
el2.click()

el3 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Activity']")))
el3.click()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).setAsVerticalList().scrollToEnd(5)')

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).setAsVerticalList().scrollToBeginning(5)')

# deviceSize = driver.get_window_size()
# print(deviceSize)

# screenWidth = deviceSize['width']
# screenHeight = deviceSize['height']
# print(screenHeight)
# print(screenWidth)

# startX = screenWidth/2
# endX = screenWidth/2
# startY = screenHeight*8/9
# endY = screenHeight/9

# actions = TouchAction(driver)

# actions.long_press(None, startX, startY).move_to(None, endX, endY).release().perform()

# actions.long_press(None, endX, endY).move_to(None, startX, startY).release().perform()
