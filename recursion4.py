from ast import Num


i=1
sum=0
def add():
    global i
    while i<=(Num):
        sum=sum+Num
        i=i+1
    print(sum)
    add()
Num=int(input("enter"))
add()


