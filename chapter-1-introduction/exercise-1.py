#عددی که بیشترین مقسوم علیه اول داره رو برمیگردونه
def is_prime(x):
    prime=True
    if x==2 :
        prime=True
    for i in range (2,(x//2)+1):
        if x%i==0:
            prime=False
            continue
    return prime
        
listadad=[]
for i in range (0,10):
    x=int(input())
    counter=0
    for i in range(2,x):
        if x%i==0:
            if is_prime(i):
                counter+=1
    listadad.append([counter,x])
    
listadad.sort(reverse=True)
print(str(listadad[0][1])+" "+str(listadad[0][0]))

            
