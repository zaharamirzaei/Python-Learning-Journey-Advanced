#نتایج جام جهانی :|
groupb=[['Iran','Spain'],['Iran','Portugal'],['Iran','Morocco'],['Spain','Portugal'],['Spain','Morocco'],['Portugal','Morocco']]
teams=[['Iran',0,0,0,0,0],['Spain',0,0,0,0,0],['Portugal',0,0,0,0,0],['Morocco',0,0,0,0,0]]
for i in range (0,6):
    x=input()
    y=x.split('-')
    if int(y[0])> int(y[1]):
        for j in range(0,len(teams)):
            if teams[j][0]==groupb[i][0]:
                teams[j][1]+=1
                teams[j][4]+=int(y[0])-int(y[1])
                teams[j][5]+=3
                break
        for j in range(0,len(teams)):
            if teams[j][0]==groupb[i][1]:
                teams[j][2]+=1
                teams[j][4]+=int(y[1])-int(y[0])
                break
    elif int(y[1])> int(y[0]):
        for j in range(0,len(teams)):
            if teams[j][0]==groupb[i][1]:
                teams[j][1]+=1
                teams[j][4]+=int(y[1])-int(y[0])
                teams[j][5]+=3
                break
        for j in range(0,len(teams)):
            if teams[j][0]==groupb[i][0]:
                teams[j][2]+=1
                teams[j][4]+=int(y[0])-int(y[1])
                break
    elif int(y[0])== int(y[1]):
        for j in range(0,len(teams)):
            if teams[j][0]==groupb[i][0]:
                teams[j][3]+=1
                teams[j][5]+=1
            elif teams[j][0]==groupb[i][1]:
                teams[j][3]+=1 
                teams[j][5]+=1  
    
teams.sort()
teams.sort(key= lambda x:x[1],reverse=True)
teams.sort(key= lambda x:x[5],reverse=True)
for sublist in teams:
    print(sublist[0]+'  wins:'+str(sublist[1])+' , loses:'+str(sublist[2])+' , draws:'+str(sublist[3])+' , goal difference:'+str(sublist[4])+' , points:'+str(sublist[5]))
