def drink(num):
    if num<=14:
        print("kids drink toddy")
    elif num>14 and num<=17:
        print("cooke")
    elif num>17 and num<=21:
        print("bear")
    else:
        print("adults drink wisky")
drink(int(input("enter")))