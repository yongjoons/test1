# -*- coding: utf-8 -*-
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)#함수안에 함수를 넣어서 돌아가도록
result = fact(5)
print(result)
