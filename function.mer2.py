 def name(a):
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
    print(max)
name([3,4,5,89,34,20])