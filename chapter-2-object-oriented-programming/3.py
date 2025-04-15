#پروژه شی گرایی
import random
class Person:
    count=0
    def __init__(self,name,team) :
        self.name=name
        self.team= team
        Person.count+=1
class Player(Person):
    def get_info(self):
        print("%s at  %s " %(self.name,self.team))
u=Player('u','d')
#names=['r','t','o','q','w','p','e','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
names=['حسین ' , ' مازیار' ,' اکبر' ,' نیما' ,  'مهدی' , 'فرهاد','محمد','خشایار','میلاد','مصطفی','امین','سعید',' پویا','پوریا','رضا' ,'علی', 'بهزاد','سهیل' , 'بهروز' ,'شهروز', 'سامان', 'محسن']
teams=['A','B']
acount=0
bcount=0
for i in range(0,len(names)):
    x=names[i]
    y=random.choice(teams)
    if y=="A" and acount<12:
        acount +=1
        names[i]=Player(x,y)
    elif y=="B" and bcount<12:
        bcount +=1
        names[i]=Player(x,y)
    elif y=="B" and bcount==12:   
        y='A'
        acount +=1
        names[i]=Player(x,y)
    elif y=="A" and acount==12:   
        y='B'
        names[i]=Player(x,y)
        bcount +=1
for i in range(0,len(names)):
    names[i].get_info()

    
    

