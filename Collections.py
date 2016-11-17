


#1.
import collections
import sys
from collections import Counter

number_of_shoes=int(input())
shoe_sizes=collections.Counter(map(int,input().split()))
number_of_customers=int(input())

total=0
for i in range(number_of_customers):
    size,pay=map(int,input().split())
    if shoe_sizes[size]:
        total=total+pay
        shoe_sizes[size]=shoe_sizes[size]-1
print (total)

#2. Got Help From the internet here
from collections import defaultdict
import collections
import sys
from collections import Counter
n,m=map(int,input().split())

d = defaultdict(list)
for i in range(1,n+1):
    d[input()].append(str(i))
for j in range(m):
    temp=str(input())
    if temp in d:
        print (' '.join(d[temp]))
    else:
        print("-1")

#3.
import collections
from collections import namedtuple
n=int(input())
index =input().split().index("MARKS")
total=0
for _ in range(n):
    total=total+int(input().split()[index])
print (total/ n)

#4. Got Help from The Internet Here

import sys
from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    [s, m] = input().strip().rsplit(maxsplit=1)
    if s in d:
        d[s] += int(m)
    else:
        d[s] = int(m)

for k, v in d.items():
    print(k, v)


#5. Got Help from the Internet Here
import sys
from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
print(len(d))
print(*d.values())

#6.
import sys
from collections import deque
d = deque()
n=int(input())
for i in range(n):
    line = input().split()
    if line[0] == "append":
        d.append(line[1])
    elif line[0] == "pop":
        d.pop()
    elif line[0] == "popleft":
        d.popleft()
    elif line[0] == "appendleft":
        d.appendleft(line[1])
for i in d:
    print(i , end=" ")

#8.1 Used the Class , Idea from the Internet

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*string) for string in OrderedCounter(sorted(input())).most_common(3)]
#8.2 Help from the Internet
from collections import Counter
print ('\n'.join([x[0]+' '+str(x[1]) for x in sorted(Counter(list(input().strip())).items(),key=lambda x: (-x[1],x[0]))[:3]]))







