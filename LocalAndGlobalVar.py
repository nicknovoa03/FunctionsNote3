# assigning a value to a variable makes it a local to the function
def funcA():
    y = 50  # assignment makes this a local
    funcB()
    print("A: x =", x, "y =", y)


def funcB():
    print("B: x =", x, "y =", y)  # referenced the global


x = 10
y = 20
funcA()
print("Outside: x =", x, "y =", y)
