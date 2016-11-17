

#1. Hello World 
print("Hello, World!")

#2. Reading Input

import sys, io
s=raw_input() 
print(s)

#3 Python If Else

import sys
N = int(raw_input().strip())
if(N%2!=0):
    print("Weird")
if(N%2==0):
    if(N==2 or N==3 or N==4 or N==5):
        print("Not Weird")
    if(N>=6 and N <=20):
        print("Weird")
    if(N>20):
        print("Not Weird")

#4. Arithmatic Operators

import sys
n1=input()
#n1=int(n1)
n2=input()
#n2=int(n2)
print(n1+n2)
print(n1-n2)
print(n1*n2)

#5. Python Division
import sys
a=input()
a=int(a)
b=input()
b=int(b)

print(a//b)
print(a/b)

#6. Loops
import sys
a=input()
a=int(a)
for i in range(0,a):
    print (i*i)

#7. Functions
import sys
def is_leap(year):
    year=int(year)
    leap = False
    # Write your logic here
    if year%4==0 and year%100!=0:
        leap=True
    if year%100==0 and year%400==0 and year%4==0:
        leap=True
    return leap


#8. Function Printing
import sys
print(*range(1, int(input())+1), sep='')

































