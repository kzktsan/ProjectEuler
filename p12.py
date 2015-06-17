def make_prime_list(num) : 
	prime_list = [2]
	for n in range(3, num+1) :

		prime_flag = True

		for prime in prime_list : 
			if n % prime == 0 : 
				prime_flag = False
				break

		if prime_flag :
			prime_list.append(n)

	return prime_list

def make_prime_multi_list(num) : 
	prime_list = make_prime_list(num)
	multi_list = []

	for prime in prime_list : 
		multi = 0
		sub = num
		while True : 
			if sub == 0 :
				break
			elif sub % prime == 0 : 
				sub = sub / prime
				multi += 1
			else :
				break

		multi_list.append(multi)

	i = 0

	while True : 
		if i == len(prime_list) :
			break
		elif multi_list[i] == 0 :
			multi_list.pop(i)
			prime_list.pop(i)
		else :
			i += 1

	return [prime_list, multi_list]

def check_divi_num(num) : 

	prime_multi_list = make_prime_multi_list(num)
	divi_num = 1

	for i in range(0, len(prime_multi_list[0])) : 
		divi_num = divi_num * (prime_multi_list[1][i] + 1)

	return divi_num

def tri(num) :

	return (num * (num + 1))/2

def func(num) : 
	i = 1
	while True :
		tri_num = tri(i)
		if check_divi_num(tri_num) >= num : 
			print check_divi_num(tri_num)
			break
		else : 
			i += 1

	return tri(i)

print func(5)
