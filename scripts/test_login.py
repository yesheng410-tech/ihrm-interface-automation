import unittest
from parameterized import parameterized
from api.login_api import IhrmLoginApi
from common.assert_util import common_assert
from common.login_schema import success_schema, error_schema
from common.read_jsondata import read_json
from config import BASE_DIR
import jsonschema


class TestIhrmLogin(unittest.TestCase):
    data = BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_json(data))
    def test_login(self, remark, res_body, status_code, success, code, message):

        resp = IhrmLoginApi.get_login(res_body)
        print(f"{remark}：{resp.json()}")
        common_assert(self, resp, status_code, success, code, message)

        try:
            if success:
                jsonschema.validate(instance=resp.json(), schema=success_schema)
            else:
                jsonschema.validate(instance=resp.json(), schema=error_schema)
            print(f"用例[{remark}]: 全量字段校验通过")
        except Exception as err:
            print(f"用例[{remark}]： 全量字段校验失败，错误信息{str(err)}")

