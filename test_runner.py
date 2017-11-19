import unittest
from concurrent.futures import ThreadPoolExecutor
import android_web_test
import android_app_test
import ios_web_test
import ios_app_test
import sys


def parallel_execution(self, *tests):
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test))

    with ThreadPoolExecutor(max_workers=10) as executor:
        list_of_suites = list(suite)
        for test in range(len(list_of_suites)):
            test_name = str(list_of_suites[test])
            return executor.submit(unittest.TextTestRunner().run, list_of_suites[test])


res = parallel_execution(0, ios_app_test.IosAppTest, ios_web_test.TestWebsiteiOSSafari, android_app_test.AndroidAppTest, android_web_test.TestWebsiteAndroidChrome)

if str(res.result()).find("errors=0") > -1 and str(res.result()).find("failures=0") > -1:
    print("All tests passed!")
    sys.exit(0)
else:
    print("Some tests failed!")
    sys.exit(1)

