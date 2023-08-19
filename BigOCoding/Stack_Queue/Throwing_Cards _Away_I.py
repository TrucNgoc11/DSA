from collections import deque
from typing import Deque, List


def helper(num_list: Deque[int]) -> List[int]:
	ans = []
	while len(num_list) > 1:
		ans.append(num_list.popleft())
		num_list.append(num_list.popleft())
	ans.append(num_list[0])
	return ans


def solve() -> None:
	while True:
		n = int(input())
		if n == 0:
			break
		else:
			num_list = deque()
			for i in range(1, n + 1):
				num_list.append(i)

		result = helper(num_list)
		print("Discarded cards: ", result)
		print("Remaining card: ",result.pop())



solve()

