# -*- coding:utf-8 -*-
import requests

URL_GET = 'http://www.baidu.com/s'


def para_requests():
    # 构建请求参数
    para = {'wd': 'lolicon', }

    # 发送请求  get/post
    response = requests.get(URL_GET, params=para)
    # response = requests.post(URL_GET, data={'key1': 'val', 'key2': 'val'})
    # json 数据
    # response = requests.post(URL_GET, json={'key1': 'val', 'key2': 'val'})

    # 处理响应
    print('info:')
    print(response.headers)
    print('status code:')
    print(response.status_code)
    print(response.reason)  # OK
    print('req body:')
    print(response.text)
    # 如果是 json 数据
    # response.json()


def temp():
    response = requests.get(URL_GET, params={'wd': 'test'})
    print(response.request.headers)
    print(response.url)


def cust_req():
    from requests import Request, Session

    headers = {'User-Agent': 'fack2.1'}
    req = Request('GET', URL_GET, headers=headers)
    prep = req.prepare()  # 准备

    print(prep.body)
    print(prep.headers)

    # 使用 Session 进行发送
    s = Session()
    resp = s.send(prep)

    print(resp.status_code)
    print(resp.request)
    print(resp.text)


if __name__ == '__main__':
    print('run...')
    para_requests()
