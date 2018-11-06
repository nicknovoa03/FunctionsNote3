# Specifying nonlocal and global to allow variable assignment
def funcA():
    def funcB():
        nonlocal x
        global y
        x += 5
        y += 5
        print("B: x =", x, "y =", y)
    x = 11
    y = 21
    funcB()
    print("A: x =", x, "y =", y)

x = 10
y = 20
funcA()
