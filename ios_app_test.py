import unittest
from appium import webdriver
import os


class IosAppTest(unittest.TestCase):
    test_name = "iOS App Test with Python"
    dc = {}
    # if you have configured an access key as environment variable,
    # use the line below. Otherwise, specify the key directly.
    accessKey = os.environ['SEETEST_IO_ACCESS_KEY']
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['app'] = 'http://d242m5chux1g9j.cloudfront.net/EriBank.ipa'
        self.dc['bundleId'] = 'com.experitest.ExperiBank'
        self.dc['platformName'] = 'ios'
        self.dc['autoDismissAlerts'] = True
        self.driver = webdriver.Remote('https://beta.seetest.io:443/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.find_element_by_xpath("xpath=//*[@text='Username']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@text='Password']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@text='loginButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='makePaymentButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Phone']").send_keys('123456')
        self.driver.find_element_by_xpath("xpath=//*[@text='Name']").send_keys('Test')
        self.driver.find_element_by_xpath("xpath=//*[@text='Amount']").send_keys('10')
        self.driver.find_element_by_xpath("xpath=//*[@text='Country']").send_keys('US')
        self.driver.find_element_by_xpath("xpath=//*[@text='sendPaymentButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Yes']").click()

    def tearDown(self):
        if self.driver is not None:
            print(self.driver.capabilities.get("reportUrl"))
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
