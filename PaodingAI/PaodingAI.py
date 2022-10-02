"""
_csrf-frontend: yLJIL8mHoDhkUgw3bIpoefjZCr9gIuXEdxv-8wvBUKGm2h93vsT2Shw4ORoUxC44kOprjC1avL4cTZCdTbADlw==
LoginForm[username]: asimovasimov
LoginForm[password]: asimovasimov

curl -X POST -d 'api_dev_key=NrTIaNdai-v2PlCNVmYuC4ZplXKBwBYX' -d 'api_paste_code=test' -d 'api_option=paste' "https://pastebin.com/api/api_post.php"

"""
from lxml import etree

import requests


class PasteBin:
    def __init__(self):
        self.headers = {
            'content-type': 'application/x-www-form-urlencoded',
            "Cookie": "_ga=GA1.2.1940645826.1631332573; _pbjs_userid_consent_data=3524755945110770; __gads=ID=bc0ad8ab2ae1dfa4:T=1631332926:S=ALNI_Ma0Y81mAVniVOugNWEi0i4SG5FdcQ; _gid=GA1.2.1758058695.1632304494; __viCookieActive=true; cf_chl_prog=a12; cf_clearance=vWwwDuVTEWAD6Ktwruc6c6_bXuZbX2jLxO34lwSAtGo-1632304688-0-150; _csrf-frontend=b55497ac118efe2ccdb59316046e28de0ee290680fd29a90f34be7a66efbddefa%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%229S3DnGAVKLyUgE2zaTsgqwGuOWMPgJML%22%3B%7D; pastebin-frontend=df0f0cde852e903935c83df879cf667c; cto_bidid=Sb9kWV8lMkZNVVZEdHJGdDI3WThDYzNWMWpUSzlMRFBMNWJTYmduNXJmJTJGaGtLZ3RCSE1tQUlTTmw2QzFOcE82cDg2Wjc3VVJrVmRLMFVhUjdGdmx2RDB2bk9QcEduOXhMcmhUQ0tla1FqTXd6dzN0R0UlM0Q; cto_bundle=qd7InV9jeVJSV25sJTJGVTIlMkZhSXdwaXE3SXZoZGc3Qlgzc0k5RGZqWVdHM1N0cjRiVnBhQzhWdDl6T0RHN3lYdUlqNEZvRm8yOTRrNWVLcFJ3RmhiaiUyRmh1M2NGb3MlMkJEOVFZZ0lRYW91R3dmMzF1WXVmaFIxMnIlMkJuQ3ZwaGdxOG43ZFJhOHR6QWJMMXB1Q2o3M1NpUFFUZ2ZnT1lBJTNEJTNE",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        }
        self.username = 'asimovasimov'
        self.password = 'asimovasimov'
        self.csrf_token = None
        self.session_login = None
        self.session_login_status = 0
        self.api_key = None
        self.user_key = None

    def get_csrf_token(self):
        get_url = 'https://pastebin.com/login'

        req = requests.get(get_url, headers=self.headers)
        if req.status_code == 200:
            root = etree.HTML(req.text)
            try:
                csrf_token = root.xpath('//meta[@name="csrf-token"]/@content')
                if csrf_token:
                    self.csrf_token = csrf_token[0]
                    return "get csrf_token successful"
                else:
                    return "csrf_token not found"
            except Exception as e:
                print(e)
        else:
            return "get csrf_token failed"

    def login(self):
        if self.csrf_token:
            url = "https://pastebin.com/login"
            data = {
                "_csrf-frontend": str(self.csrf_token),
                "LoginForm[username]": self.username,
                "LoginForm[password]": self.password
            }
            self.session_login = requests.session()
            try:
                req = self.session_login.post(url, headers=self.headers, data=data)
                if req.status_code == 200:
                    self.session_login_status = 1
                    return "login successful"
                else:
                    return "login failed"
            except Exception as e:
                print(e)
        else:
            return "csrf_token not found"

    def get_api_key(self):
        if self.session_login_status == 1:
            doc_api = 'https://pastebin.com/doc_api'
            req1 = self.session_login.get(doc_api)
            root_doc_api = etree.HTML(req1.text)
            try:
                api_key = root_doc_api.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div[6]/div//text()')
                if api_key:
                    self.api_key = api_key[0]
                    return "get api_key successful"
                else:
                    return "api_key not found"
            except Exception as e:
                print(e)
        else:
            return "session_login_status err"

    def get_user_key(self):
        url = "https://pastebin.com/api/api_login.php"
        data = {
            "api_dev_key": self.api_key,
            "api_user_name": self.username,
            "api_user_password": self.password
        }
        rep = self.session_login.post(url, data=data)
        if rep.status_code != 200:
            raise Exception("get api_user_key fail")
        self.user_key = rep.text

    def post_content(self, api_paste_code, api_paste_name):
        """
        :param api_paste_code: 黏贴内容
        :param api_paste_name: 名称
        :return:
        """
        self.get_user_key()
        data = {"api_dev_key": self.api_key,
                "api_option": "paste",
                "api_paste_code": api_paste_code,
                "api_paste_name": api_paste_name,
                "api_user_key": self.user_key,
                # public = 0，unlisted = 1，private = 2
                "api_paste_private": 2}
        url = "https://pastebin.com/api/api_post.php"
        r = self.session_login.post(url, data=data)
        if r.status_code != 200:
            raise Exception("create paste fail")
        else:
            return "create paste successful"
        return ""


def get_busybox():
    headers = {
        'Authorization': 'Basic TGlMZWk6SUxvdmVIYW5NZWltZWk=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
    }
    url = 'http://120.79.245.107:3112/msg.txt'
    try:
        req = requests.get(url, headers=headers)
        return str(req.text)
    except Exception as e:
        print(e)
        return ''


if __name__ == '__main__':
    content = get_busybox()
    if content:
        p = PasteBin()
        print(p.get_csrf_token())
        print(p.login())
        print(p.get_api_key())
        print(p.post_content(content, "test"))
