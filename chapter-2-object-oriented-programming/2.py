#سن کنونی
import datetime
birthday=input()
birthday=birthday.split("/")
today=datetime.date.today()

if len(birthday[0])!=4 or len(birthday[1])!=2 or  len(birthday[2])!=2:
    print('WRONG')
elif int(birthday[1])>12 or int(birthday[1])<1 or int(birthday[2])>31 or int(birthday[2])<1:
    print('WRONG')
elif today.year-int(birthday[0]) <0:
    print('WRONG')
else:
    
    urage=today.year-int(birthday[0])
    month=int(birthday[1])-today.month
    day= int(birthday[2])-today.day
    if today.year==int(birthday[0]):
        urage=0
    #elif month==0:
        #if day<0:
            #urage-=1
    #elif month<0:
        #urage-=1
    print(urage)
