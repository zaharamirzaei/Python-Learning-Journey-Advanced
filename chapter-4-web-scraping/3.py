#web scraping

import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
    
product=input('enter search name in digikala:')
dbname=input('enter database name :')
user=input('enter the name of user:')
table=input('enter table name:')
#اتصال به دیتابیس
cnx=mysql.connector.connect(user= '%s'%user,password='',host='127.0.0.1',database='%s'%dbname)
#اتصال به سایت
r=requests.get('https://www.digikala.com/search/?q=%s'%product)
soup=BeautifulSoup(r.text,'html.parser')
inf=soup.find_all('div',attrs={'class':"c-product-box__content"})
counter=0
for i in inf:
    name=i.find('a',attrs={ 'class':"js-product-url"})
    price=i.find('div',attrs={'class':"c-price__value-wrapper"})
    name=re.sub(r'\s','',name.text)
    price=re.sub(r'\s','',price.text)
    cursor=cnx.cursor()
    query='INSERT INTO %s VALUES(\'%s\',\'%s\')'%(table,name,price)
    cursor.execute(query)
    cnx.commit()
    counter+=1
    if counter==20:
        break
cnx.close()



