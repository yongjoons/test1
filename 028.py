seq1='ATGTTATAG'
new1=''
for s in seq1:
    if s=='A':
        new1 +='T'
    elif s=='T':
        new1 +='A'
    elif s=='C':
        new1 +='G'
    elif s=='G':
        new1 +='C' #you can use dictionary.
print(seq1)
print(new1)
'''rev_seq=''
compdic={'A':'T','T':'A','C':'G','G':'C'}
for s in seq1:
    rev_seq +=compdic[s]
print(rev_seq)'''# using dictionary 
