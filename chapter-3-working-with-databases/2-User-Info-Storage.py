#ذخیره ایمیل در پایگاه داده
import mysql.connector
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
#معتبر بودن ایمیل را چک میکند
def check(email):
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False
dbname=input('enter dabtabase name:')
username=input('enter username:')
email=input('enter email:')
while check(email)==False:
    email=input("please enter the correct format of email like \"sara1993@yahoo.com\" :")

epassword=input('enter your password:')

cnx=mysql.connector.connect(user= '%s'%username,password='',host='127.0.0.1',database='%s'%dbname)
query='INSERT INTO userpass VALUES (\'%s\',\'%s\')' %(email,epassword)
cursor=cnx.cursor()
cursor.execute(query)
cnx.commit()
#query='SELECT * FROM userpass';
#cursor.execute(query)
#for (email,password) in cursor :
    #print('%s pass is %s'%(email,password))

cnx.close()
