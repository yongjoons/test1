seq1='agtttatag'
print(seq1.index('tt'))

for i in range(0,len(seq1),1):
    if seq1[i:i+2]=='tt':
        print(i ,i+1 ,seq1[i:i+2])
        continue
