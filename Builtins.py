

#1.
# Enter your code here. Read input from STDIN. Print output to STDOUT
#import numpy as np
string=input().split()
m,n= map(int, string)
results=[]
for i in range(n):
    string=input().split()
    lis=list(map(float,string))
    results.append(lis)
for student in zip(*results):
    avg=sum(student)/len(student)
    print (avg)

#2.
string=raw_input().split()
N,M=map(int,string)
data=[]
for i in xrange(N):
    data.append(raw_input().split(' '))
k=int(raw_input())
data.sort(key=lambda x: int(x[k]))
for i in xrange(N):
    for j in xrange(M):
        print data[i][j],
    print "\n",

