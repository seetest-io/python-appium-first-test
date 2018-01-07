import unittest
import os
from appium import webdriver


class TestWebsiteiOSSafari(unittest.TestCase):
    dc = {}
    test_name = 'Test Mobile Website on iOS Safari'
    # if you have configured an access key as environment variable,
    # use the line below. Otherwise, specify the key directly.
    accessKey = os.environ['SEETEST_IO_ACCESS_KEY']
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['platformName'] = 'ios'
        self.dc['browserName'] = 'safari'
        self.dc['autoDismissAlerts'] = True
        self.driver = webdriver.Remote('https://cloud.seetest.io:443/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.get('https://amazon.com')
        if self.driver.capabilities['device.category'] == 'TABLET':
            self.driver.find_element_by_xpath("//*[@name='field-keywords']").send_keys('iPhone')
            self.driver.find_element_by_xpath("//*[@text='Go']").click()
        else:
            self.driver.find_element_by_xpath("//*[@name='k']").send_keys('iPhone')
            self.driver.find_element_by_xpath("//*[@value='Go']").click()

    def tearDown(self):
        if self.driver is not None:
            print(self.driver.capabilities.get("reportUrl"))
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

