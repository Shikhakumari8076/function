i=1
def table():
    global i
    while i<=10:
        b=n*i
        print(n,"*",i,"=",b)
        i=i+1
        table()
n=int(input("enter"))
table()
