def square_add(num) : 
	result = 0
	for n in range(1, num+1) : 
		result += n * n
	return result

def add_square(num) : 
	add_sum = (num * (num+1))/2
	return add_sum*add_sum


print add_square(100)-square_add(100)
