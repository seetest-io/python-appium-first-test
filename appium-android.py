import unittest
import time
from appium import webdriver


class AndroidTest(unittest.TestCase):
    projectName = "<PROEJCT_NAME>"
    accessKey = "<ACCESS_KEY>"
    dc = {}
    driver = None

    def setUp(self):
        self.dc['accessKey'] = self.accessKey
        self.dc['projectName'] = ''
        self.dc['platformName'] = 'Android'
        self.dc['app'] = 'cloud:<BUNDLE_ID>'
        self.dc['appPackage'] = '<BUNDLE_ID>'
        self.dc['appActivity'] = '<ACTIVITY>'
        self.driver = webdriver.Remote('https://cloud.experitest.com:443/wd/hub', self.dc)

    def testYourAndroidApp(self):
        time.sleep(0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()