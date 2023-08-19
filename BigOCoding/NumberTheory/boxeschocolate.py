from typing import List


def solve():
	t = int(input())
	for _ in range(t):
		f, b = map(int, input().split())
		res = 0
		for j in range(b):
			nums = list(map(int, input().split()))
			cnt = 1
			for k in range(1, len(nums), 1):
				cnt = (cnt * nums[k]) % f
			res = (res + cnt) % f
		print(res)


solve()