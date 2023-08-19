from typing import List


def solve():
	n, k = map(int, input().split())
	a = list(map(float, input().split()))
	result = num_search(a, 1.0 * k)
	print('%.6f' % result)


def num_search(num_list: List[float], k: float):
	left, right = 1.0 * min(num_list), 1.0 * max(num_list)
	er = 1e-6
	right += er
	while left + er < right:
		mid = (left + right) / 2.0
		#print(mid, left, right)
		if is_valid(num_list, mid, k):
			left = mid
		else:
			right = mid
	return left


def is_valid(num_list: List[float], mid: float, k: float) -> bool:
	need = 0.0
	can_give = 0.0
	for val in num_list:
		if val >= mid:
			can_give += (val - mid)
		else:
			need += (mid - val)
	return can_give * (1.0 - k / 100) >= need



solve()