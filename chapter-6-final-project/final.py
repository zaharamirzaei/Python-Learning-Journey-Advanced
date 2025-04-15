import requests
from sklearn import tree
from bs4 import BeautifulSoup
import re
import mysql.connector
from requests import models
cnx=mysql.connector.connect(user= 'root',password='',host='127.0.0.1',database='bama')
for i in range(1,25):
    r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page=%i'%i)
    soup=BeautifulSoup(r.text,'html.parser')
    inf=soup.find_all('div',attrs={ 'class':"card-content vehicle-card-body order-3"})
    for i in inf:
        sal=i.find('span',attrs={ 'class':"vehicle-card-year font-size-1"})
        sal=int(sal.text)
        brand=i.find('span',attrs={'class':"vehicle-header-make-model text-truncate"})
        model=re.sub(r'.*\s','',brand.text)
        brand=re.sub(r'\s+.*','',brand.text)
        price=i.find('div',attrs={'class':"heading-3 margin-y-1 font-weight-bold"} )
        price=re.sub(r'\$','',price.text)
        price=int(re.sub(r',','',price))
        karkard=i.find('div',attrs={'data-test':'vehicleMileage'})
        karkard=re.sub(r'\s*miles\s*','',karkard.text)
        karkard=int(re.sub(r',','',karkard))
        #print(brand)
        cursor=cnx.cursor()
        query='INSERT INTO carinfo VALUES(\'%s\',\'%s\',\'%i\',\'%i\',\'%i\')'%(brand,model,sal,karkard,price)
        cursor.execute(query)
        cnx.commit()

#machine learning part
query='SELECT * FROM carinfo'
cursor=cnx.cursor()
cursor.execute(query)
x=[]
y=[]

ubrand=input('enter car brand:')
umodel=input('enter car model:')
usal=int(input('enter car year:'))
ukarkard=int(input('enter car Mileage:'))
for (brand,model,sal,karkard,price) in cursor:
    if brand==ubrand and umodel==model:
        x.append([sal,karkard])
        y.append(price)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

newdata=[[usal,ukarkard]]
answer=clf.predict(newdata)
print('your car price is abour %i $'%answer[0])
cnx.close()