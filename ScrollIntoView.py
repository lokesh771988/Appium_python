from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.alert import Alert
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

el3 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Alert Dialogs']")))
el3.click()

el4 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='OK Cancel dialog "
                                                                  "with a long message']")))
el4.click()

