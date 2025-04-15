#لیست اسامی المپیاد
tedad=int(input())
olist=[]
for i in range(0,tedad):
    x=input()
    y=x.split('.')
    name=y[1][0].upper()+y[1][1:].lower()
    olist.append([y[0],name,y[2]])
olist.sort()
for i in range (0,tedad):
    print(olist[i][0]+" "+olist[i][1]+" "+olist[i][2])