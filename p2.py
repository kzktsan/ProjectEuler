def fib(limit):
	var1 = 1
	var2 = 2
	result = 2
	while True : 
		temp = var1 + var2
		
		if temp > limit:
			break
		elif temp % 2 == 0:
			result += temp

		var1 = var2
		var2 = temp

	return result

print fib(10)

