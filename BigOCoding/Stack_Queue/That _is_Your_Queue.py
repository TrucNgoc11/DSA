from collections import deque
from typing import List


def helper(arr) -> List[int]:
	pool = deque()
	ans = []
	for action, val in arr:
		if action == "N":
			pool.append(val)
		else:

	return ans


def solve() -> None:
	case = 0
	while True:
		case += 1
		n, t = map(int, input().split())
		if n == 0:
			break
		else:
			arr = []
			idx = 1
			for _ in range(t):
				x = list(input().split())
				if len(x) == 2:
					arr.append(tuple([x[0], int(x[1])]))
				else:
					arr.append(("N", idx))
					idx += 1

			result = helper(arr)
			print(f"Case {case}:")
			for i in result:
				print(i)


solve()




