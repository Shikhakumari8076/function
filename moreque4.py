def fun():
    if a>b and a>c:
        print(a,"greater")
    elif b>a and b>c:
        print(b,"greater")
    elif c>a and c>b:
        print(c,"greater")
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
fun()