def add_number_list(list,list1):
    i=0
    j=0
    l=[]
    while i<len(list):
        s=list[i]+list1[j]
        l.append(s)
        j=j+1
        i=i+1
    print(l)
add_number_list([50,60,10],[10,20,13])
