import unittest
from api.login_api import LoginApi
from utils import assert_common, read_login_data
import logging
from parameterized import parameterized
# import parameterized


class TestIHRMLoginParameterized(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(read_login_data)
    def test01_login(self, mobile, password, http_code, success, code, message):
        response = self.login_api.login(mobile, password)
        logging.info("登陆接口返回数据为：{}".format(response.json()))
        # 断言
        assert_common(self, response, http_code, success, code, message)
