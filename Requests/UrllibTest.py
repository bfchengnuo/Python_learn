# -*- coding:utf-8 -*-
from urllib import request, parse

URL_GET = 'http://www.baidu.com/s'


def para_urllib():
    # 构建请求参数
    para = parse.urlencode({'wd': 'lolicon', })
    print(para)

    # 发送请求
    response = request.urlopen('?'.join([URL_GET, '%s']) % para)

    # 处理响应
    print('info:')
    print(response.info())
    print('status code:')
    print(response.getcode())
    print('req body:')
    print(response.read().decode('utf-8'))
    # 2.x 版本
    # print(''.join([line for line in response.readlines]))


if __name__ == '__main__':
    print('run...')
    para_urllib()
