def its_change(n1,n2):
    i=0
    j=0
    l=[]
    while i<len(n2):
        s=n1[i]*n2[j]
        l.append(s)
        j=j+1
        i=i+1
    print(l)

its_change([5,10,50,20],[2,20,3,5])
