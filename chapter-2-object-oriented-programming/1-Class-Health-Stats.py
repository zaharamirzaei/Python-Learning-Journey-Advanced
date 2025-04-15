#برنامه سلامت
from statistics import mean
class Class:
    def __init__(self,name) :
        self.name = name
        self.count=int(input()) 
        self.ages=input().split()
        for i in range(0,self.count):
            self.ages[i]=float(self.ages[i])
        self.ghads=input().split()
        for i in range(0,self.count):
            self.ghads[i]=float(self.ghads[i])
        self.vazns=input().split()
        for i in range(0,self.count):
            self.vazns[i]=float(self.vazns[i])

    def get_avgs(self):
        self.age_avg=mean(self.ages)
        print(self.age_avg)
        self.ghad_avg=mean(self.ghads)
        print(self.ghad_avg)
        self.vazn_avg=mean(self.vazns)
        print(self.vazn_avg)
def Compare(a,b):
    if a.ghad_avg > b.ghad_avg:
        print (a.name)
    elif a.ghad_avg < b.ghad_avg:
        print (b.name)
    elif a.ghad_avg == b.ghad_avg:
        if a.vazn_avg > b.ghad_avg:
            return b.name
        elif a.ghad_avg < b.ghad_avg:
            return a.name
        else:
            print ('Same')

A=Class('A')
B=Class('B')
A.get_avgs()
B.get_avgs()
Compare(A,B)
