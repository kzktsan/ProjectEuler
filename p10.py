# coding: UTF-8
import math

# 単純なアルゴリズムで素数リストを求める関数
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

# エラトステネスの篩で素数リストを求める関数
def make_prime_list_Erasto(num) : 
	prime_list = []
	candi_list = []
	for i in range(2, num+1) : 
		candi_list.append(i)

	while True : 
		if candi_list[0] > math.sqrt(num) :
			prime_list.extend(candi_list)
			break

		tmp = candi_list[0]
		prime_list.append(candi_list[0])
		candi_list.pop(0)

		i = 0
		while True :
			if i == len(candi_list) : 
				break
			else :
				if candi_list[i] % tmp == 0 :
					candi_list.pop(i)
				else :
					i += 1


		'''
		for i in range(0, len(candi_list)) : 
			if candi_list[i] % tmp == 0 :
				candi_list[i] = -1
		
		while -1 in candi_list : 
			candi_list.remove(-1)
		'''

	return prime_list


result = 0
prime_list = make_prime_list_Erasto(10)

for prime in prime_list : 
	result = result + prime

print result
#print prime_list