import pymysql

db = pymysql.connect("localhost", "root", "testmysql")
cursor = db.cursor()
# cursor.execute("create database indexdb;")
cursor.execute("use indexdb;")
# cursor.execute("create table t1(id int,name char(20))")
n = 1
name = 'shuai'
while n < 100:
    insert_name = name + str(n)
    cursor.execute("insert into t1 values('%s', '%s');" % (n, insert_name))
    n += 1
db.commit()
cursor.close()
db.close()