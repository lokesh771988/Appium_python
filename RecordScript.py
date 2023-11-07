from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
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

wait1 = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
el2 = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Create contact")))
el2.click()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First name")').send_keys('Lokesh1')
#el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='First name']")
#el3.send_keys("Lokesh1")
el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']")
el4.send_keys("9876543210")
el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='Save']")
el5.click()

driver.quit()