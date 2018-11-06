# nested funcB references nonlocal x in funcA
def funcA():
    def funcB():
        print("B: x =", x, "y =", y)

    x = 11
    funcB()
    print("A: x =", x, "y =", y)


x = 10
y = 20
funcA()
