li=[3,1,1,2,0,0,2,3,3]
dict1={}
count=0
for x in li:
    print(x ,dict1)
    if x in dict1:
        dict1[x] +=1
    else :
        dict1[x]=1
print(dict1)

'''for x in li:
    if x==0:
        
        dict1[x] =dict1[x]+1
    elif x==1:
        count +=1
        dict1[x]=count'''
print(dict1)
