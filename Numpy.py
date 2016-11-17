

#2.
import numpy
numbers=input().split()
lis=list(map(int,numbers))
array=numpy.array(lis)
print (numpy.reshape(array,(3,3)))

#3.
import numpy as np
N,M=map(int,input().split())
array=np.array([input().split() for i in range(N)],dtype=int) #List Comprehension to Create a Numpy Array
print (array.transpose())
print (array.flatten())

#4.
import numpy as np
N,M,P=map(int,input().split()) #Mapping Values of M,N and Pto Integers
array1=np.array([input().split() for i in range(N)],dtype=int)
array2=np.array([input().split() for i in range(M)],dtype=int)
print(np.concatenate((array1,array2)))

#5.
import numpy as np
N=list(map(int,input().split()))
array1=np.zeros(N,dtype=int)
array2=np.ones(N,dtype=int)
print (array1)
print (array2)

#6.
import numpy
N,M=map(int,input().split())
print(numpy.eye(N,M,k=0))

#7.
import numpy as np
N,M=map(int,input().split())
A=np.array([input().split() for i in range(N)],dtype=int) #List Comprehension to Create a Numpy Array
B=np.array([input().split() for i in range(N)],dtype=int) #List Comprehension to Create a Numpy Array
print (A+B)
print (A-B)
print (A*B)
print (A//B)
print (A%B)
print (A**B)

#8.
import numpy as np
l=list(map(float,(input().split())))
print (np.floor(np.array(l)))
print (np.ceil(np.array(l)))
print (np.rint(np.array(l)))


#9.
import numpy as np
N,M=map(int,(input().split()))
A=np.array([input().split() for i in range(N)],dtype=float) #List Comprehension to Create a Numpy Array
B=np.sum(A, axis = 0)
C=int(np.prod(B, axis = 0))
print (C)
#10.

import numpy as np
N,M=map(int,(input().split()))
A=np.array([input().split() for i in range(N)],dtype=float) #List Comprehension to Create a Numpy Array
B=np.min(A, axis = 1) 
C=int(np.max(B))
print (C)

#11.

import numpy as np
N,M=map(int,(input().split()))
A=np.array([input().split() for i in range(N)],dtype=float) #List Comprehension to Create a Numpy Array
print (np.mean(A, axis = 1))
print (np.var(A, axis = 0))
print (np.std(A, axis = None))



#12.

import numpy as np
N=int(input())
A=np.array([input().split() for i in range(N)],dtype=int) #List Comprehension to Create a Numpy Array
B=np.array([input().split() for i in range(N)],dtype=int) #List Comprehension to Create a Numpy Array
print (np.dot(A,B))


#13.

import numpy as np
A=np.array(list(map(int,input().split())))
B=np.array(list(map(int,input().split())))
print (np.inner(A,B))
print(np.outer(A,B))


#14.
import numpy as np
matrix=list(map(float,input().split()))
x=float(input())
print(np.polyval(matrix,x))

#15.

import numpy as np
N=int(input())
array=np.zeros((N,N))
for i in range(N):
    array[i,:]=np.array(input().split(" "), dtype=float)
print (np.linalg.det(array))

















