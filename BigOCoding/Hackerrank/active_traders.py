from typing import List


def solve():
	n = int(input())
	customers = []
	for _ in range(n):
		cus = input()
		customers.append(cus)
	print(mostActive(customers))

def mostActive(customers):
	customers = customers.sort()
	cnt = [0] * len(customers)
	new_list = []
	for idx, val in enumerate(customers):
		cnt[idx] = find_last(customers, val) - find_first(customers, val)
		new_list.append(customers[find_last(customers, val)])

	ans = []
	for a in new_list:
		for val in cnt:
			if val == max(cnt):
				ans.append(a)
				cnt.pop(val)
	return ans


def find_first(arr: List[str], target: str):
	if not arr:
		return -1
	n = len(arr)
	l, r = -1, n - 1
	while l + 1< r:
		m = (l + r) // 2
		if arr[m] <= target:
			r = m
		else:
			l = m
	return r if arr[m] == target else -1


def find_last(arr: List[str], target: str):
	l, r = find_first(arr, target), len(arr)
	while l + 1 < r:
		m = (l + r) // 2
		if arr[find_first(arr, target)] == arr[m]:
			l = m
		else:
			r = m
	return l


solve()