import unittest
from htmltestreport import HTMLTestReport

from config import BASE_DIR
from scripts.test_login import TestIhrmLogin

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestIhrmLogin))

runner = HTMLTestReport(BASE_DIR + "/report/ihrm_login_test.html",
                        description="登录接口测试用例",
                        title="ihrm登录接口测试")
runner.run(suite)

