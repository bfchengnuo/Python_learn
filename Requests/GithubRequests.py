# -*- coding:utf-8 -*-
import json

import requests

URL_MAIN = 'https://api.github.com/'


def url_build(para):
    return ''.join([URL_MAIN, para])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    response = requests.get(url_build('users/bfchengnuo'))
    # print(response.text)
    print(better_print(response.text))


if __name__ == '__main__':
    print('run....')
    request_method()
