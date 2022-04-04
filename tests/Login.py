import string
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("udid, deviceName, systemPort", [('a4f23bf20221', 'POCO M3', '8203'), ('emulator-5554', 'Pixel 4', '8204')])
def test_Login(udid, deviceName, systemPort):

    caps = {"platformName": "Android", "platformVersion": "10.0", "deviceName": deviceName, 'udid': udid, 'systemPort': int(systemPort),
            "appPackage": "com.swaglabsmobileapp", "appActivity": "com.swaglabsmobileapp.MainActivity",
            "automationName": "UiAutomator2", "orientation": 'PORTRAIT'}
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    driver.implicitly_wait(15)
    #webview = driver.contexts.last
    #driver.switch_to.context(webview)
    driver.find_element_by_xpath("//android.widget.EditText[@content-desc='test-Username']").send_keys("standard_user")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@content-desc='test-Password']").send_keys("secret_sauce")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='test-LOGIN']").click()
    driver.implicitly_wait(3)
    MobileElement = driver.find_element_by_xpath("hierarchy/android.widget.FrameLayout/android.widget.LinearLayout");
    if MobileElement.isDisplayed():

        {
            print("Element found and test Passed")
        }
    else:
        {
                print("Element not found and test failed")
        }
    driver.quit()


def test_Invalid_Login(udid, deviceName, systemPort):

    caps = {"platformName": "Android", "platformVersion": "10.0", "deviceName": deviceName, 'udid': udid, 'systemPort': int(systemPort),
            "appPackage": "com.swaglabsmobileapp", "appActivity": "com.swaglabsmobileapp.MainActivity",
            "automationName": "UiAutomator2", "orientation": 'PORTRAIT'}
    driver = webdriver.Remote('', caps)
    driver.implicitly_wait(15)
    #webview = driver.contexts.last
    #driver.switch_to.context(webview)
    driver.find_element_by_xpath("//android.widget.EditText[@content-desc='test-Username']").send_keys("test1")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.widget.EditText[@content-desc='test-Password']").send_keys("test2")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='test-LOGIN']").click()
    driver.implicitly_wait(3)
    Error_Msg = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='test-Error message']/android.widget.TextView").text
    assert Error_Msg == "Username and password do not match any user in this service.***********//)