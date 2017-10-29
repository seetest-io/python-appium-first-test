import unittest
from concurrent.futures import ThreadPoolExecutor
import ios_web_test
import android_web_test
import android_app_test
import ios_app_test


def parallel_execution(self, *tests):
    suite = unittest.TestSuite()

    for test in tests:
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test))

    with ThreadPoolExecutor(max_workers=10) as executor:
        list_of_suites = list(suite)
        for test in range(len(list_of_suites)):
            test_name = str(list_of_suites[test])
            executor.submit(unittest.TextTestRunner().run, list_of_suites[test])

parallel_execution(0,
                   ios_app_test.IosAppTest,
                   android_app_test.AndroidAppTest,
                   android_web_test.TestWebsiteAndroidChrome,
                   ios_web_test.TestWebsiteiOSSafari)