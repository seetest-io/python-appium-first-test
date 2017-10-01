import unittest
import time
from appium import webdriver


class Untitled(unittest.TestCase):
    projectName = "<PROJECT_NAME>"
    accessKey = "<ACCESS_KEY>"
    dc = {}
    driver = None

    def setUp(self):
        self.dc['accessKey'] = self.accessKey
        self.dc['projectName'] = ''
        self.dc['deviceQuery'] = '@os="ios"'
        self.dc['projectName'] = self.projectName
        self.dc['app'] = 'cloud:<BUNDLE_ID>'
        self.dc['bundleId'] = '<BUNDLE_ID>'
        self.dc['platformName'] = 'ios'
        self.driver = webdriver.Remote('https://cloud.experitest.com:443/wd/hub', self.dc)

    def testUntitled(self):
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
