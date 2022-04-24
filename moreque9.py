def harshad():
    sum=0
    c=num
    while c>0:
        b=c%10
        sum=sum+b
        c=c//10
    if num%sum==0:
        print(sum,"true")
    else:
        print("false")
num=int(input("enter"))
harshad()



def harshad():
    i=1
    a=0
    while i<=100:
        b=i
        sum=0
        while b>0:
            a=b%10
            sum=sum+a
            b//=10
        if i%sum==0:
            print(i,end=' ')
        i=i+1
harshad()
