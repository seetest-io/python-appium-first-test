import unittest
import time
from appium import webdriver
import os


class AndroidAppTest(unittest.TestCase):
    test_name = "Android App Test with Python"
    accessKey = os.environ['accessKey']
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
        time.sleep(0)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()