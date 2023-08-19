from typing import List


def check_power(n: int) -> bool:
	if (n - 1) & n == 0:
		return True
	return False


def solve():
	t = int(input())
	for _ in range(t):
		n = int(input())
		list_num = map(int, input().split())
		for num in list_num:
			if check_power(num):
				print("YES")
				break
			else:
				print("NO")
				break


solve()