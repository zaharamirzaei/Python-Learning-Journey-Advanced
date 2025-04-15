#نظرسنجی ژانر مورد علاقه
ganrs={'Horror':0, 'Romance':0, 'Comedy':0, 'History':0 , 'Adventure':0 , 'Action':0}
tedad=int(input())
for i in range(0,tedad):
    x=input()
    y=x.split()
    for i in range(1,len(y)):
        ganrs[y[i]]=int(ganrs[y[i]])+1
ganr_result=[]
for item in ganrs:
    ganr_result.append([item,ganrs[item]])
ganr_result.sort()
ganr_result.sort(reverse=True, key=lambda x: x[1])
for i in range(0,len(ganr_result)):
    print(ganr_result[i][0]+' : '+str(ganr_result[i][1]))
