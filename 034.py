li=[3,1,1,2,0,0,2,3,3]
max_v=0
min_v=100
for x in li:
    if max_v < x:
        max_v = x
    elif min_v >x:
        min_v = x
print('maxval: ',max_v,'minval: ', min_v)

'''print('max: ',max(l),'min: ',min(l))''' #this method is best
