#کلمات شاخص

x=input()
y=x.split()
counter=1
uplist=[]
noghte='.'
virgool=','
up=False
for word in y[1:]:
    if word[0].isupper() and y[counter-1][-1] != noghte:
        uplist.append([counter+1,word])
        up=True
    counter+=1
if up:
    for word in uplist:
        if word[1][-1]== noghte or word[1][-1]== virgool:
            print(str(word[0])+":"+word[1][0:-1])
        else:
            print(str(word[0])+":"+word[1])
else:
    print('None')


