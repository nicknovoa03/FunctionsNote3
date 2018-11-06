# global statement makes the variable a global, allowing it to be assigned
def funcA():
    global y
    y = 50
    funcB()
    print("A: x =", x, "y =", y)


def funcB():
    print("B: x =", x, "y =", y)


x = 10
y = 20
funcA()
print("Outside: x =", x, "y =", y)
