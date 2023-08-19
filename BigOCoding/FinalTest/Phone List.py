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
	test_case = int(input())
	for _ in range(test_case):
		result = True
		n = int(input())
		numbers = []
		for _ in range(n):
			n1 = input()
			numbers.append(n1)
		quick_sort(numbers, 0, n - 1)
		for i in range(n - 1):
			if numbers[i + 1].startswith(numbers[i]):
				result = False
				break
		if result is True:
			print("YES")
		else:
			print("NO")


solve()

