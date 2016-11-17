

#1. Lists
import sys
#########
n = int(input())
l = []
for i in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print (l)

#2. Tuples
print hash(tuple(map(int, input().strip().split(" "))))

#3. Lists Comprehension

import sys

x, y, z, n = (int(input()) for i in range(4))
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ]) #third Level Loop Inside List


#4. Second Largest Number

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

input()
lis = sorted(set(map(int, input().strip().split()))) 
print(lis[len(lis)-2])


#5. Nested Lists

marksheet = []
for i in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1] #list comprehension
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


#6. Percentage
n = int(input())
mydict = {}
for line in range(n):
    info = raw_input().split(" ")
    score = map(float, info[1:])
    mydict[info[0]] = sum(score) / float(len(score))

print ("%.2f" % round(mydict[raw_input()],2))





