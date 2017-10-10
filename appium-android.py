import unittest
import time
from appium import webdriver
import os


class AndroidAppTest(unittest.TestCase):
    test_name = "Android App Test with Python"
    accessKey = os.environ['ACCESS_KEY']
    dc = {}
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['platformName'] = 'Android'
        self.dc['app'] = 'cloud:com.experitest.ExperiBank/.LoginActivity'
        self.dc['appPackage'] = 'com.experitest.ExperiBank'
        self.dc['appActivity'] = '.LoginActivity'
        self.driver = webdriver.Remote('https://cloud.experitest.com:443/wd/hub', self.dc)

    def testYourAndroidApp(self):
        self.driver.press_keycode(82)
        self.driver.find_element_by_xpath("xpath=//*[@id='usernameTextField']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@id='passwordTextField']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@id='loginButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Make Payment']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='phoneTextField']").send_keys('123456')
        self.driver.find_element_by_xpath("xpath=//*[@id='nameTextField']").send_keys('Test')
        self.driver.find_element_by_xpath("xpath=//*[@id='amountTextField']").send_keys('10')
        self.driver.find_element_by_xpath("xpath=//*[@id='countryTextField']").send_keys('US')
        self.driver.find_element_by_xpath("xpath=//*[@text='Send Payment']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Yes']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()