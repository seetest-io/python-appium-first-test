import unittest
import os
from appium import webdriver


class TestWebsiteAndroidChrome(unittest.TestCase):
    dc = {}
    test_name = 'Test Mobile Website on iOS Safari'
    # accessKey = os.environ['SEETEST_IO_ACCESS_KEY']
    accessKey = 'eyJ4cC51IjoxNjUwLCJ4cC5wIjoxNDM1LCJ4cC5tIjoiTVRRNU5UQXhOelV3T0RreE1BIiwiYWxnIjoiSFMyNTYifQ.eyJleHAiOjE4MTY0MzI4MDcsImlzcyI6ImNvbS5leHBlcml0ZXN0In0.JBVpm1JBc8AEHSJm3nY8qv-7Orx0MfSN6D9BsxmfcSA'
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['platformName'] = 'ios'
        self.dc['browser'] = 'safari'
        self.driver = webdriver.Remote('https://cloud.experitest.com:443/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_xpath("xpath=//*[@name='q']").send_keys('mobile automation testing')
        self.driver.find_element_by_xpath("xpath=//*[@name='btnG']").click()
        self.driver.implicitly_wait(5000)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

