# 导包
import time
import unittest, app
# 实例化测试套件
from script.test_ihrm_login import TestIHRMLogin
# from script.test_ihrm_emp import TestEmp
from script.test_irhm_emp_parameterized import TestEmpParameterzied
from tools import HTMLTestRunner

suite = unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestEmpParameterzied))

# 设置测试报告的路径和名称
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestRunner
    runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=1, title="IHRM人力资源管理系统接口测试报告",
                                           description="测试登陆接口和员工管理模块")
    # 使用Runner运行测试套件生成测试报告
    runner.run(suite)
