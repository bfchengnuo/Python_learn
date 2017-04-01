# -*- coding: utf-8 -*-
import os
import sys
from os.path import basename

from qiniu import Auth
from qiniu import etag
from qiniu import put_file

access_key = ''
secret_key = ''
bucket_name = ''
link_prefix = ''


# 读取配置文件
def load_file():
    global access_key, secret_key, bucket_name, link_prefix
    key_file = open("key.txt")
    key_lines = key_file.readlines()
    for key_line in key_lines:
        key_key = key_line[:key_line.find('=')]
        key_val = key_line[key_line.find('=') + 1:]
        key_val = key_val.replace('\r', '').replace('\n', '')
        if key_key == 'AccessKey':
            access_key = key_val
        elif key_key == 'SecretKey':
            secret_key = key_val
        elif key_key == 'name':
            bucket_name = key_val
        elif key_key == 'url':
            link_prefix = key_val


# 读取文件列表参数
def load_para():
    is_false = True
    if len(sys.argv) <= 1:
        print('请确认输入路径参数！')
        return
    for path in sys.argv[1:]:
        # 文件路径和文件名
        local_file = path.replace('\\', '/')
        key = basename(local_file)
        upload(local_file, key, is_false)
        is_false = False


# 上传文件
def upload(local_file, key, flag=True):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 生成上传 Token，可以指定过期时间等，上传空间、文件名
    token = q.upload_token(bucket_name, key, 3600)

    ret, info = put_file(token, key, local_file)
    # print(info)
    # print(ret)
    assert ret['key'] == key
    assert ret['hash'] == etag(local_file)
    print('![' + key + '](' + link_prefix + ret['key'] + ')')
    if flag:
        add_to_clipboard('![' + key + '](' + link_prefix + ret['key'] + ')')


# 写入剪切板
def add_to_clipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


if __name__ == '__main__':
    load_file()
    print('开始上传...\n\n')
    load_para()
