import sys
sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())
i=0
def fun():
    global i
    i=i+1
    print("hello",i)
    fun()
fun()
