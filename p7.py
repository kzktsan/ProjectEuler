def show_prime(num):
	prime_list = [2]
	prime_count = 1
	i = 3
	while True : 
		prime_flag = 1

		for p in prime_list : 
			if i % p == 0 :
				prime_flag = 0
				break

		if prime_flag == 1 :
			prime_list.append(i)
			prime_count += 1

		if prime_count >= num : 
			break
		else :
			i += 1

	return prime_list[num-1]

print show_prime(10001)