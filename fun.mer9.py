def perfect():
    x=1
    while x<=1000:
        i=1
        sum=0
        while i<x:
            if x%i==0:
                sum=sum+i
            i=i+1
        if sum == x:
            print(x,"perfect no.")
        x=x+1
perfect()
