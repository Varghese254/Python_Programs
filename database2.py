import pymysql
conn=pymysql.connect(host='localhost',use='root',password="",db="xy")
cursur=conn.cursor()
sql="""create table dept(deptno int,deptname char(20),location char(25))"""
cursor.execute(sql)
conn.commit()
conn.close()
