# coding: UTF-8

#　与えられた値までの素数のリストを返す
def prime(num):
	prime_list = [2]
	for i in range(2, num+1):
		prime_flag = 1

		for p in prime_list : 
			if i % p == 0 :
				prime_flag = 0
				break

		if prime_flag == 1 :
			prime_list.append(i)

	return prime_list 

def func(num):
	prime_list = prime(num)
	prime_len = len(prime_list)
	multi_list = []

	for i in range(0, prime_len):
		multi_list.append(0)

	for n in range(1, num+1):
		for j in range(0, prime_len):
			n_value = n
			p_value = prime_list[j]
			mul_count = 0

			while True :
				if n_value ==0 : 
					break  
				elif n_value % p_value == 0 :
					mul_count = mul_count + 1
					n_value = n_value / p_value
				else : 
					break
				
			if mul_count > multi_list[j] :
				print n
				multi_list[j] = mul_count

	result = 1
	for k in range(0, prime_len):

		for l in range(1, multi_list[k] + 1):
			result = result * prime_list[k]


	print prime_list
	print multi_list

	return result


print func(20)