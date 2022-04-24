def shownum(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum=sum+i
            print(i)
        i=i+1
    print(sum)
shownum(int(input("enter")))