from typing import List
# Time complexity: O(nlogn) cho average case and worst case
# Space: O(n)


def divide(arr: List[int], left: int, right: int) -> None:
	if left >= right:
		return
	mid = (left + right) // 2
	divide(arr, left, mid)
	divide(arr, mid + 1, right)
	merge(arr, left, mid, right)


def merge(arr: List[int], left: int, mid: int, right: int) -> None:
	tmp = []
	i, j = left, mid + 1
	while i <= mid and j <= right:
		if arr[i] <= arr[j]:
			tmp.append(arr[i])
			i += 1
		else:
			tmp.append(arr[j])
			j += 1
	while i <= mid:
		tmp.append(arr[i])
		i += 1
	while j <= right:
		tmp.append(arr[j])
		j += 1
	arr[left: right + 1] = tmp


def solve():
	arr = [1, 5, 7, 4, 3]
	divide(arr, 0, len(arr) - 1)
	print(arr)


solve()
