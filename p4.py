result = 0
ans1 = 0
ans2 = 0

for var1 in range(100, 1000):
	for var2 in range (var1, 1000):
		value = var1 * var2
		value_str = str(value)
		value_len = len(value_str)
		flag = 0
		for n in range(0, (int)(value_len/2)+1):
			if value_str[n] != value_str[value_len - (n+1)]:
				flag = 1

		if flag == 0 and value > result :
			ans1 = var1
			ans2 = var2
			result = value
 
print ans1
print ans2
print result
