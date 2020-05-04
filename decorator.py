def display(a):
    print(a)
def parentdeco(fun):
    print("in dec")
    def forattribute(a):
        dec1=fun(a)
        print("dec1"+dec1)
    return forattribute
x1=parentdeco(display)
@parentdeco
def another(g):
    print(g)
    return g
another("eeee")

