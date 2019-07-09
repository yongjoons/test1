#result=1
def myfact(n):
    while n>0 :
        answer=n
        n=n-1
        result= answer * n
        
        return result

myfact(5)
print(myfact(5))
