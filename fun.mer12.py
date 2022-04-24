def shownumber():
    i=0
    while i<=n:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
n=int(input("enter"))
shownumber()
