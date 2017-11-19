import unittest
from concurrent.futures import ThreadPoolExecutor
import android_web_test
import android_app_test
import ios_web_test
import ios_app_test
import sys


failed_tests = []


def parallel_execution(self, *tests):
    list_of_suite_results = []
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test))

    with ThreadPoolExecutor(max_workers=10) as executor:
        list_of_suites = list(suite)
        for test in range(len(list_of_suites)):
            list_of_suite_results.append(executor.submit(unittest.TextTestRunner().run, list_of_suites[test]))
    return list_of_suite_results


parallel_execution(0, ios_app_test.IosAppTest, ios_web_test.TestWebsiteiOSSafari, android_app_test.AndroidAppTest,
                         android_web_test.TestWebsiteAndroidChrome)





