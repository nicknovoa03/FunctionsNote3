# function printList prints the contents of its argument
# if it encounters a negative value, it returns
def printList(lis):
    for x in lis:
        if x < 0:
            return
        print(x)


nums = [10, 20, 30, -25, 50]
printList(nums)
