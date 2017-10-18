import unittest
import os
from appium import webdriver


class TestWebsiteAndroidChrome(unittest.TestCase):
    dc = {}
    test_name = 'Test Mobile Website on Android Chrome'
    #if you have configured an access key as environment variable,
    #use the line below. Otherwise, specify the key directly.
    accessKey = os.environ['SEETEST_IO_ACCESS_KEY']
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['platformName'] = 'android'
        self.dc['browserName'] = 'chrome'
        self.driver = webdriver.Remote('https://cloud.experitest.com:443/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.press_keycode(82)
        self.driver.get('https://google.com')
        self.driver.find_element_by_xpath("xpath=//*[@name='q']").send_keys('mobile automation testing')
        self.driver.find_element_by_xpath("xpath=//*[@name='btnG']").click()
        self.driver.implicitly_wait(5000)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

