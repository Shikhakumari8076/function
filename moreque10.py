def maximum():
    i=0
    while i<len(marks):
        j=0
        while j>i:
            if marks[i][j]>max:
                max=marks[i][j]
                j=j+1
            i=i+1
        print(max)
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
maximum()