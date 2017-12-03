import unittest
from appium import webdriver
import os


class AndroidAppTest(unittest.TestCase):
    test_name = "Android App Test with Python"
    dc = {}
    # if you have configured an access key as environment variable,
    # use the line below. Otherwise, specify the key directly.
    accessKey = os.environ['SEETEST_IO_ACCESS_KEY']
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['platformName'] = 'Android'
        self.dc['app'] = 'http://d242m5chux1g9j.cloudfront.net/eribank.apk'
        self.dc['appPackage'] = 'com.experitest.ExperiBank'
        self.dc['appActivity'] = '.LoginActivity'
        self.driver = webdriver.Remote('https://beta.seetest.io:443/wd/hub', self.dc)

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
        self.driver.find_element_by_xpath("xpath=//*[@id='button1']").click()

    def tearDown(self):
        if self.driver is not None:
            print(self.driver.capabilities.get("reportUrl"))
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()