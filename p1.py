limit = 1000
total = 0

def func(num):
	if (num % 3 == 0 or num % 5 == 0):
		global total
		total += num

for num in range (1, limit):
	func(num)

print total