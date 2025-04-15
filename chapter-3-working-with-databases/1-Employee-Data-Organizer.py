#اطلاعات کارمندان
#برای اتصال به دیتابیس موقت روی زمپ از دستور پایین در محیط کامند استفاده میکنیم
#cd c:\xampp\mysql\bin
#mysql.exe -u root
import mysql.connector
username=input("enter user name:")
dbname=input("enter database name:")
cnx=mysql.connector.connect(user= '%s'%username,password='',host='127.0.0.1',database='%s'%dbname)
cursor=cnx.cursor()
query='SELECT name,height,weight FROM employee ORDER BY height DESC ,weight ;'
cursor.execute(query)
for (name,height,weight) in cursor:
    print("%s %i %i"%(name,height,weight))
cnx.close()
