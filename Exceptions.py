
#1.
test_cases=int(input())
for i in range(test_cases):   
    try:
        string=input().split()
        a,b= map(int, string)
        print(a//b)      
    except (ZeroDivisionError, ValueError) as e: #Multiple Exceptions, Same as Java 
        print("Error Code:", e)
