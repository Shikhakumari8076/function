def unq(l):
    i=0
    m=[]
    while i<len(l):
        if l[i] not in m:
            m.append(l[i])
        i=i+1

    print(m)
        
unq([1,6,8,9,9,5,3,6,5,8,8,8])













