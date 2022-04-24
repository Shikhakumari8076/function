def fectorail(n):
    if n==0:
        return 1
    else:
        return n*fectorail(n-1)
n=int(input("enter"))
res=fectorail(n)
print(res)
fectorail()    
