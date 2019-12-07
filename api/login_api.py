import requests


class LoginApi:

    def __init__(self):
        self.login_url = "http://182.92.81.159" + "/api/sys/login"
        self.headers = {"Content-Type": "application/json"}
        pass

    def login(self, mobile, password):
        login_data = {
            "mobile": mobile,
            "password": password
        }
        return requests.post(self.login_url, json=login_data, headers=self.headers)

    def login_none_params(self):
        return requests.post(self.login_url, headers=self.headers)

    def login_extra_params(self):
        return requests.post(self.login_url,
                             json={"mobile": "13800000002",
                                   "password": "123456",
                                   "extra_params": "测试"},
                             headers=self.headers)

    def login_less_params(self):
        return requests.post(self.login_url, json={"password": "123456"}, headers=self.headers)
