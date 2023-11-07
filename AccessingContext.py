import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': "uiautomator2",
    'deviceName': 'Android',
    'appPackage': 'com.socialnmobile.dictapps.notepad.color.note',
    'appActivity': 'com.socialnmobile.colornote.activity.Main',
    'language': 'en',
    'locale': 'US',
    'app:browserName': 'Chrome'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

wait = WebDriverWait(driver, 10)

el3 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='SKIP']")))
el3.click()

el1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.FrameLayout["
                                                                 "@content-desc='More']/android.widget.ImageView")))
el1.click()

el2 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Like us on "
                                                                 "Facebook']")))
el2.click()

print(driver.contexts)
print(driver.context)
time.sleep(5)
driver.switch_to.context('WEBVIEW_chrome')

text = driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Log in']").text

# el4 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Log in']")))
print(text)

el5 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@text='󱤅']")))
el5.click()

el6 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@text='About']")))
el6.click()

el7 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@text='Bio']")))
print(el7.text)

driver.back()
driver.back()
driver.back()
