import pymysql
conn=pymysql.connect(host='localhost',user='root',password="",db="xz")
cursor=conn.cursor()
sql="""create table dept(deptno int,deptname char(20),location char(25))"""
cursor.execute(sql)
conn.commit()
conn.close()
