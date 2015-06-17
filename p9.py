def square(a) : 
	return a*a

def func(sum_num) : 
	for a in range(1, sum_num-1) : 
		for b in range(1, sum_num - a) : 
			c = sum_num - (a+b)
			if square(a) + square(b) == square(c) :
				print a
				print b
				print c
				return a*b*c

	return "Not Found"


print func(10)
