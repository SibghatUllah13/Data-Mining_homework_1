

#1.
import sys
#
s=0
number_of_plants=int(input())
string=input()
lis=str.split(string," ")
new_list = []
for item in lis:
    new_list.append(float(item))

plants_heights=set(new_list)
print (sum(plants_heights)/len(plants_heights))

#2.
import sys
############### Set1
number_of_entries_set1=int(input())
string=input()
set1 =set(list(map(int, string.split())))
## Set 2
number_of_entries_set2=int(input())
string2=input()
set2 =set(list(map(int, string2.split())))
#########
set3=set1.union(set2)
set4=set1.intersection(set2)
####
set5=set3.difference(set4)
for n in sorted(list(set5)):
    print (n)

#3. 
n, m = input().split()
array = input().split()
seta = set(input().split())
setb = set(input().split())
print (sum([(i in seta) - (i in setb) for i in array])) #List Comprehension


#4.
import sys
s=set()
n=int(input())
i=0
while(1):
    if(i<n):
        s.add(input())
        i=i+1
    else:
        break
print (len(s))

#5.
import sys
n=int(input())
s = set(map(int,input().split()))
N=int(input())
for i in range(N) :
    choice=input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove" :
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :
        s.discard(int(choice[1]))
print (sum(s))

#6.

import sys
n= int(input())
list1 =  input().split()
b= int(input())
list2 =input().split()
union = set(list1).union(list2)
count = 0
for i in union:
    count=count+1
print (count)


#7.
import sys
n= int(input())
list1 =  input().split()
b= int(input())
list2 =input().split()
union = set(list1).intersection(list2)
count = 0
for i in union:
    count=count+1
print (count)

#8.
import sys
n= int(input())
list1 =  input().split()
b= int(input())
list2 =input().split()
union = set(list1).difference(list2)
count = 0
for i in union:
    count=count+1
print (count)


#9.
import sys
n= int(input())
list1 =  input().split()
b= int(input())
list2 =input().split()
union = set(list1).symmetric_difference(list2)
count = 0
for i in union:
    count=count+1
print (count)

#10 Got Help From the Internet for this Question
number_of_entries = int(input())
seta = set(map(int,input().split(" ")))
number_of_other_sets = int(raw_input())

for i in range(number_of_other_sets):
    cmd, args =input().split(" ")
    setb = set(map(int,input().split(" ")))
    eval('seta.'+cmd+'(setb)')

print (sum(seta))


#11.
import sys
d=input()  
a=input().split()
s1=set()
s2=set()  
for i in a:
    if  i in s1:
        s2.add(i);
    else:
        s1.add(i);
s3=s1.difference(s2);
print (list(s3)[0]);

#12.
for i in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))


#13. Got Help from the Internet here
a = set(map(str, input().split(" ")))
is_strict_superset = []
for i in range(int(input())):
     is_strict_superset.append(a.issuperset(set(map(str, input().split(' ')))))
print(all(is_strict_superset))


































