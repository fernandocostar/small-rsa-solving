import math
from fractions import gcd

"""
RSA 4 BYTES SOLVING
"""

def candidate_range(a):
    n = a
    cur = 5
    incr = 2
    while cur < n+1:
        yield cur
        cur += incr
        incr ^= 6

def sieve(end):
    prime_list = [2, 3]
    sieve_list = [True] * (end+1)
    for each_number in candidate_range(end):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for multiple in range(each_number*each_number, end+1, each_number):
                sieve_list[multiple] = False
    return prime_list

def check_divisors(vet, n):
	l = []
	for each in vet:
		if n%each == 0:
			l.append(each)
	return l

n, e, c = map(int, input().split(" "))
aux = check_divisors(sieve(n), n)
k = (aux[0]-1)*(aux[1]-1)

d = -1
for d in range(1, k):
	if((e*d) % k == 1):
		break
print(pow(c, d, n))