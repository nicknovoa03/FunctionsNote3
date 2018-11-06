def sumList (lis):
	sum = 0
	for x in lis:
		sum += x
	return sum

nums = [10, 20, 30]
sum = sumList(nums)
print("sum is", sum)
