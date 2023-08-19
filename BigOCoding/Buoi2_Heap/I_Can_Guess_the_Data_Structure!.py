import collections, heapq
from typing import List, Tuple


def helper(num_list: List[Tuple]) -> List[bool]:

	st = [] #stack
	qu = collections.deque() #queue
	pool2 = []
	is_stack = is_queue = is_max_heap = True
	for action, val in num_list:
		if action == 1:
			st.append(val)
			qu.append(val)
			heapq.heappush(pool2, -val)
		else:
			if len(st) == 0:
				is_stack = is_queue = is_max_heap = False
				break
			else:
				if is_stack and val != st.pop():
					is_stack = False
				if is_queue and val != qu.popleft():
					is_queue = False
				if is_max_heap and val != -heapq.heappop(pool2):
					is_max_heap = False
	ans = [is_stack, is_queue, is_max_heap]
	return ans


def solve():
	while True:
		try:
			n = int(input())
		except Exception as ex:
			#print("loi: ", ex)
			break
		num_list = []
		for _ in range(n):
			x = map(int, input().split())
			num_list.append(tuple(x))

		re = helper(num_list)
		if (re[0] + re[1] + re[2]) == 0:
			print("impossible")
		elif (re[0] + re[1] + re[2]) > 1:
			print("not sure")
		elif re[0]:
			print("stack")
		elif re[1]:
			print("queue")
		else:
			print("priority queue")


solve()






