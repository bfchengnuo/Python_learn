import re

# pa = re.compile(r'^\d{2}-\d{3,4}$',re.I)
# ma = pa.match('43-1234  45-3421')

# 进行预编译，不区分大小写
pa = re.compile(r'^(\d{2})-(\d{3,4})$',re.I)
ma = pa.match('43-1234')

# 编译执行一起,如果要复用还是拆开比较好
# pa = re.match(r'abc','str')

if ma:
    print(ma.group(0))
    print(ma.group(1))
    print(ma.groups())
else:
    print("无匹配")
