def calculator():
    if num_x =="+":
        print(x+y)
    elif num_x=="-":
        print(x-y)
    elif num_x=="*":
        print(x*y)
    elif num_x=="//":
        print(x//y)
x=int(input("enter"))
y=int(input("enter"))
num_x=(input("enter any opratator"))
calculator()