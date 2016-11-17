#1.
import sys
string=input()
print (string.swapcase())
#2.
import sys
string=input()
string =string.split(" ")
string="-".join(string)
print (string)
#3.
import sys
first_name=input()
last_name=input()
print ("Hello "+ first_name+" "+last_name+"! You just delved into python.")
#4.
import sys
string=input()
i, c = input().split()
print (string[:int(i)] + c + string[int(i)+1:])
#5.
Str=input()
key= input()
count=0
for c in range(len(Str)):
    if Str[c:c+len(key)] == key: 
        count += 1
print (count)
#6.
string=input()
print any(c.isalnum()  for c in string)
print any(c.isalpha() for c in string)
print any(c.isdigit() for c in string)
print any(c.islower() for c in string)
print any(c.isupper() for c in string)
#7. Got Help from Internet for This Question
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#8.
import textwrap
s = input()
w = int(input())
l = " ".join(textwrap.wrap(s,w))
print(textwrap.fill(l,w))


#10.
n = int(input())
w = len(str(bin(n)).replace('0b',''))

for i in range(1, n+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')
    o = oct(int(i)).replace('0','', 1).rjust(w, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
    j = str(i).rjust(w, ' ')
    print (j, o, h, b)


#12.
import string
string = input()
for x in string[:].split():
    string = string.replace(x, x.capitalize())
print(string)


#14.
import string
s = input()
k = int(input())
temp = []
size = 0
for obj in s:
    size = size+1
    if obj not in temp:
        temp.append(obj)
    if size == k:
        print (''.join(temp))
        temp = []
        size = 0










