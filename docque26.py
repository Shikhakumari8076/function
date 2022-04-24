def div(num):
    if num%3 ==0 and num%5==0:
        print("fizz-buzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
div(int(input("enetr")))