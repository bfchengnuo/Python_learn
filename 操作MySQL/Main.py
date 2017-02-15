import pymysql

# print(pymysql)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='12300', db='test', charset='UTF8')
# 关闭自动commit，避免一句sql当作一个事物，默认关闭
# conn.autocommit(False)
cur = conn.cursor()
# cur.execute("select version()")
cur.execute("select * from temp")

# 返回的数据是元组的元组，可以进行遍历
# for i in cur:
#     print("id:%d 姓名：%s" %i)

print(cur.rowcount)
# 返回一行数据，将指针移动一行
rs = cur.fetchone()
print(rs)
# 返回指定的行数 对于当前指针
rs = cur.fetchmany(3)
print(rs)
# 返回全部，当前指针以下
rs = cur.fetchall()
print(rs)

cur.close()
conn.close()
