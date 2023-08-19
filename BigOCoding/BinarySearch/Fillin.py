from typing import List


def split_container(nums:List[int], m: int) -> int:
	if not nums:
		return 0
	if len(nums) < m:
		return 0
	left, right = max(nums) - 1, sum(nums)
	while left + 1 < right:
		mid = (left + right) // 2
		if is_valid(nums, mid, m):
			right = mid
		else:
			left = mid
	return right


def is_valid(nums: List[int], mid: int, m: int) -> int:
	cur_sum, count = 0, 1
	for val in nums:
		if cur_sum + val <= mid:
			cur_sum += val
		else:
			count += 1
			cur_sum = val
	return count <= m


def solve():
	while True:
		try:
			n, k = map(int, input().split())
			nums = list(map(int, input().split()))
			ans = split_container(nums, k)
			print(ans)
		except EOFError:
			break


solve()