def calculate():
  #  num=int(input("eneter"))
    i=1
    while i<=num:
        j=1
        fac=1
        while j<=i:
            fac=fac*j
            j=j+1
        i=i+1
    print(fac)
num=int(input("eneter"))
calculate()