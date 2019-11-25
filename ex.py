import pymysql
comfig = {
    'host': '192.168.1.156',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'ecshop',
    'charset':'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}
db=pymysql.connect(**comfig)
cur=db.cursor()
sql="SELECT * FROM ecs_admin_user"
cur.execute(sql)
data=cur.fetchall()
db.close()

print(data)
