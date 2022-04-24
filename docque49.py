def squares():
    i=1
    while i<=10:
        n=int(input("enter"))
        if n%2==0:
            mul = n*100
            print(mul,"even")

        else:
            mul1=n*-1
            print(mul1,"odd")
        i=i+1
squares()
