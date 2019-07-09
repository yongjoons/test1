# -*- coding: utf-8 -*-
import sys
num=int(sys.argv[1])
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else :
       return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(num))
'''
li=[0,1]
for i in range(8):
    val=l[-2]+l[-1]
    li.append(val)
print(li)'''
