from typing import List


"""
Function tim uoc chung lon nhat greatest common divisor
"""

def gcd (a: int, b: int) -> int:
	while b != 0:
		r = a % b
		a = b
		b = r
	return a


def solve():
	m, n = map(int, input().split())
	a = [0 for i in range(m)]
	b = [0 for i in range(n)]

	day = m * n * gcd(m, n)
	happy_b = list(map(int, input().split()))
	nb = happy_b[0]
	happy_g = list(map(int, input().split()))
	ng = happy_g[0]

	for i in range(1, len(happy_b)):
		a[happy_b[i]] = 1
	for i in range(1, len(happy_g)):
		b[happy_g[i]] = 1

	for k in range(0, 2*day + 1):
		boy = k % m
		girl = k % n
		if a[boy] == 0 and b[girl] == 1:
			nb += 1
			a[boy] = 1
		if a[boy] == 1 and b[girl] == 0:
			ng += 1
			b[girl] = 1

	if (nb + ng) == (m + n):
		print("Yes")
	else:
		print("No")


solve()



