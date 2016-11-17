

#1.
import re
test_cases = int(input())
for i in range(test_cases):
    string=input()
    check=re.search(r'^[+|-]?\d*\.\d+$',(string))
    check=bool(check)
    print (check)

#2.
import re
string=input()
string = re.split("[,.]",string)
for term in string:
    if term.isdigit():  #Same as isdigit Function in Java
        print(term)

#3.
import re
string=input()
search=re.search(r'([a-zA-Z0-9])\1',string)
if (search)!=None: #If there is a Match, return the First Group, Else, Return 1
    print (search.group(1))
else:
    print ("-1")

#4.
import re
vow="AEIOUaeiou" #Vowel can be in Upper Case and Lower Case both
cons="QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm" #Consonants can also be in Upper Case and Lower Case both
pattern=r'(?=[{c}]([{v}][{v}]+)[{c}])'.format(v=vow, c=cons)
#Using lookaround '?' to build a Pattern in this Case.
match=re.findall(pattern, input())
if match: 
    for single_match in match:
        print (single_match)
else: 
    print (-1)


#5.
import re
S = input()
k = input()
pattern = re.compile(k)
r = pattern.search(S)
if not r: 
    print ("(-1, -1)")
while r: #While is used when True or False
    print ("("+str(r.start())+", "+str(r.end()-1)+")") 
    r=pattern.search(S,r.start()+1) #r=r+1, loop increment


#6.
import re
lines = int(input())
regexp=r'(?<= )(&&|\|\|)(?= )' #Using Lookaround to Create a Regexp
for i in range(lines):
    string=input()
    print (re.sub(regexp,lambda x:'and' if x.group() == '&&' else 'or', string))
    #Use re.sub, Which can be used with inline Function lambda, Which then does the required Task


#8.

import re 
test_cases=int(input())
regexp=r'[789]\d{9}$'
for i in range(test_cases):
    phone_number=input()
    if re.match(regexp,phone_number):
        print("YES")  
    else:
        print("NO")

#9.

import re
import email.utils
number=int(input())
email_regexp=r'^[a-zA-Z]+[\w_.-]*@[A-Za-z]+\.[A-Za-z]{1,3}$' #The Regexp gives us a Framkwork to Identify real Email from Fake 
for i in range(number):
    string=input()
    s=email.utils.parseaddr(string)
    match=re.match(email_regexp,s[1])
    if match:
        print(email.utils.formataddr(s))

#10.

import re
number=int(input())
hex_reg=r'#[a-fA-F\d]{6}|#[a-fA-F\d]{3}' #Regexp for Hexadecimal Color
for i in range(number):
    string=input()
    code=string[1:] 
    match=re.findall(hex_reg,code)
    if match:
        print(*match,sep='\n') #Print all Values in match , Separated by \n or new line

#11.

import re
from html.parser import HTMLParser 
class MyHTMLParser(HTMLParser):   #Got Help from the Internet for the Creation of Class /////
    def handle_starttag(self, tag, attrs):
        print ("Start :",tag)
        for attr in attrs:
            print ("->", attr[0], ">", attr[1])
    def handle_endtag(self, tag):
        print ("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for attr in attrs:
            print ("->", attr[0], ">", attr[1])
            
parser = MyHTMLParser()
regexpr=r'\<\!--.*?--\>'
html_text = str()
number=int(input())
for i in range(number):
    string=input()
    html_text=html_text+string
texts = re.sub(regexpr, "",html_text)
parser.feed(texts)

#12.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    #MY Code
    def handle_comment(self, data):
        if data.strip():
            data=str(data)
            lines=data.split("\n")
            if len(lines)>1:
                print(">>> ","Multi","-line Comment",sep="")
            else:
                print(">>> ","Single","-line Comment",sep="")
            print(*lines, sep="\n")

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
    #My Code Ends Here          
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#14.

import re 
#Got Help from the Internet for Creation of The Below RegExpr
length_regexpr=r'^[a-zA-Z0-9]{10}$'
upper_regexpr=r'(.*[A-Z].*){2,}'
numbers_regexpr= r'(.*[0-9].*){3,}'
repeat_regexpr=r'^(?:([a-zA-Z0-9])(?!.*\1))*$'
patterns=[length_regexpr,upper_regexpr,numbers_regexpr,repeat_regexpr]
reg=map(re.compile, patterns)
numbers=int(raw_input())
for i in xrange(numbers):
    ID=raw_input()
    temp=ID.strip()
    if all([r.match(temp) for r in reg]):
        print 'Valid'
    else:
        print 'Invalid'

#15.

import re
Rexpr1=r'^([456]\d{3})(\-?)(\d{4})(\2)(\d{4})(\2)(\d{4})$' #Got Help from the Internet
Rexpr2=r'^(?:([0-9])(?!\1{3,})){16}$' #Got Help from the Internet
N=int(input())
for i in range(N):
    string=input()
    if re.match(Rexpr1,string):
        string=string.replace('-','') #This is Valid
        if re.match(Rexpr2,string):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')


#16.
#Simplest Question of RegExpr
import re
postcode = input()
Regexpr1=r'^[1-9][0-9]{5}$'
Regexpr2=r'(?=(([0-9])[0-9]\2))'
Check1=re.match(Regexpr1,postcode)!=None     #Making Sure that input are Digits b/w 0-9
Check2=len(re.findall(Regexpr2,postcode))<=1 #Making Sure that Only One Digit can repeat Twice
print(Check1 and Check2)
#17.
import re
string=input().split()
n,m=map(int,string)          
Matchings=[]
Regexpr=r'[a-zA-Z0-9-\!@#\$%& ]'
Regexpr2=r'(?<=[a-zA-Z0-9])[!@#$%& ]{1,}(?=[a-zA-Z0-9])'
for i in range(n):
    string=input()
    Matchings.append(re.findall(Regexpr,string))
New_Matrix=""
for i in range(m):
    for j in range(n):
        New_Matrix=New_Matrix+Matchings[j][i]
print(re.sub(Regexpr2," ",New_Matrix))




        












