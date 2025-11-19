import requests


class IhrmLoginApi:
    @classmethod
    def get_login(cls, json_data):
        url = "https://ihrm-java.itheima.net/api/sys/login"
        resp = requests.post(url=url, json=json_data)
        return resp

