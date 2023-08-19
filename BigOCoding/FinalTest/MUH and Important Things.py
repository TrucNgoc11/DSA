from typing import List


def quick_sort(num_list: List[int], left, right):
	if left >= right:
		return
	i, j = left, right
	pivot = num_list[(left + right) // 2]
	while i <= j:
		while num_list[i] < pivot:
			i += 1
		while num_list[j] > pivot:
			j -= 1
		if i <= j:
			num_list[i], num_list[j] = num_list[j], num_list[i]
			i += 1
			j -= 1
	quick_sort(num_list, left, j)
	quick_sort(num_list, i, right)


def solve():
	n = int(input())
	num_list = list(map(int, input().split()))
	new = []
	for idx, val in enumerate(num_list):
		new.append((val, idx + 1))
	quick_sort(new, 0, n  - 1)
	res = [new[i][1] for i in range(n)]
	used = []
	for idx in range(n - 1):
		if new[idx][0]== new[idx + 1][0] :
			used.append((idx, idx + 1))
			if len(used) == 2:
				print("YES")
				print(" ".join(str(i) for i in res))
				for j, k in used:
					res[j], res[k] = res[k], res[j]
					print(" ".join(str(i) for i in res))
				quit()
	print("NO")


solve()




