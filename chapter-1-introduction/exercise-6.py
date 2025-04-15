#مترجم
n=int(input())
words={}
for i in range(0,n):
    x=input()
    y=x.split()
    for i in y[1:4]:
        words[i]=y[0]
sentence=input()
translate=''
for i in sentence.split():
    if i in words:
        translate=translate+words[i]+' '
    else:
        translate=translate+i+" "
print(translate[0:-1])
