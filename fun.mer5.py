def check_function_list(a1,a2):
    i=0
    j=0
    while i<len(a2):
        if a1[i]%2==0 and a2[j]%2==0:
            print("dono even hai")
        else:
            print("dono even nhi hai")
        j=j+1
        i=i+1
check_function_list([2,6,18,10,3,75],[6,19,24,12,3,87])
