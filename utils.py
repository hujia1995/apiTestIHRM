from requests import Response
import pymysql
import json

# 通用断言函数
import app


def assert_common(self, response, http_code, success, code, message):
    """
    @type response:Response
    """

    jsonData = response.json()  # type:dict
    # 断言响应状态码
    self.assertEqual(http_code, response.status_code)
    # 断言success
    self.assertEqual(success, jsonData.get("success"))
    # 断言code
    self.assertEqual(code, jsonData.get("code"))
    # 断言message
    self.assertIn(message, jsonData.get("message"))


class DBUtils:

    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(host, user, password, database)

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    # __enter__和__exit__这两个魔法函数是python内置函数，是在使用with语法打开对象时，要执行的函数。
    # 执行顺序：with打开时，执行__enter__函数。退出with时，执行__exit__函数
    # with open(filename, mode='r') as f: pass
    # 引用：with DBUtils() as db: db.execute()


def read_login_data():
    login_data_path = app.BASE_DIR + "/data/login_data.json"
    with open(login_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        for login_data in jsonData:
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            http_code = login_data.get("http_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")
            result_list.append((mobile, password, http_code, success, code, message))
    print("result_list的值为：", result_list)
    return result_list


def read_add_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        add_emp_data = jsonData.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list.append((username, mobile, http_code, success, code, message))

    print("add emp data: ", result_list)
    return result_list


def read_query_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        query_emp_data = jsonData.get("query_emp")
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        result_list.append((http_code, success, code, message))

    print("query emp data: ", result_list)
    return result_list

def read_modify_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        modify_emp_data = jsonData.get("modify_emp")
        username = modify_emp_data.get("username")
        http_code = modify_emp_data.get("http_code")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        result_list.append((username, http_code, success, code, message))

    print("modify emp data: ", result_list)
    return result_list

def read_delete_emp_data():
    emp_data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(emp_data_path, mode='r', encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        delete_emp_data = jsonData.get("delete_emp")
        http_code = delete_emp_data.get("http_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        result_list.append((http_code, success, code, message))

    print("delete emp data: ", result_list)
    return result_list

if __name__ == '__main__':
    read_modify_emp_data()
    read_delete_emp_data()
