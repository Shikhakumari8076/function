def prime():
    i=1
    fac=0
    while i<=num:
        if num%i==0:
            fac+=1
        i+=1
    if fac==2:
        print(num,"prime number")
    else:
        print("nhi hai")
num=int(input("enter"))
prime()