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
    'appPackage': 'com.google.android.contacts',
    'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

wait = WebDriverWait(driver, 10)
el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id"
                                                              "/permission_allow_button")))
el1.click()

element = driver.find_elements(AppiumBy.XPATH,
                               '//android.widget.TextView[@resource-id="com.google.android.contacts:id/cliv_name_textview"]')
print(len(element))

actions = TouchAction(driver)
# actions.tap(element[1]).perform().release()
actions.long_press(element[1]).perform().release()
