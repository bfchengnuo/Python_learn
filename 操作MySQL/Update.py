import pymysql

# conn相当于在客户端和服务器直接修了一条路，cur是运输的货车，当然它也是有可能出现异常的

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='12300', db='test', charset='UTF8')
# 关闭自动commit，避免一句sql当作一个事务，默认关闭
# conn.autocommit(False)
cur = conn.cursor()

try:
    cur.execute("insert into temp(name) values('测试')")
    print("执行完毕！")
    # 不进行提交数据库不会改变的，因为事务未完成
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

cur.close()
conn.close()
