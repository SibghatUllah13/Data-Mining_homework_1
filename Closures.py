#Got Help from Internet for this Question

#1.
N=int(input())
mobile_number=[]
for i in range(N):
    temp=input()
    mobile_number.append(temp)
def correction(function):
    array=[]
    def cleaner(lis):
        for m in lis:
            if len(m)==10:
                m='+91'+m
                array.append(m)
            elif len(m)==11:
                m='+91'+m[1:]
                array.append(m)
            elif len(m)==12:
                m='+'+m
                array.append(m)
            elif len(m)==13:
                array.append(m)
            else:
                print ("Something wrong with your number")
        return function(array)
    return cleaner
@ correction
def sorting(array):
    return sorted(array)
num_after=sorting(mobile_number)
for x in num_after:
    print('{} {} {}'.format(x[:3],x[3:8],x[8:]))