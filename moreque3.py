def password(strong):
    i=0
    while i<=100:
        upper="A to Z"
        lower="a to z"
        if strong== "upper" or strong=="lower":
            pass
        elif strong=="@"or strong=="#":
            print("strong password")
        else:
            print("week password")
password((input("enter any password")))


