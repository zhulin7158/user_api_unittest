import unittest
from BeautifulReport import BeautifulReport
from testcase.test_demo import demo

if __name__ == '__main__':
    suite1 =unittest.TestLoader().loadTestsFromTestCase(demo)

    suite =unittest.TestSuite(suite1)

    # unittest.TextTestRunner(verbosity=2).run(suite)
    result = BeautifulReport(suite)
    result.report(filename="测试报告",description="测试api报告",report_dir="../report",)

