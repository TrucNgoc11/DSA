from typing import List, Tuple
import heapq


def train_time(trains: List[Tuple], T: int):
	min_heap_b = []
	min_heap_a = []
	count = [0, 0]
	for (start, end, side) in trains:
		if side == 0:
			if min_heap_a and min_heap_a[0] <= start:
				heapq.heappop(min_heap_a)
			else:
				count[side] += 1
			heapq.heappush(min_heap_b, end + T)
		else:
			if min_heap_b and min_heap_b[0] <= start:
				heapq.heappop(min_heap_b)
			else:
				count[side] += 1
			heapq.heappush(min_heap_a, end + T)
	return count


def convert_int(s: str) -> int:
	hour = int(s[:2])
	mi = int(s[3:])
	return hour * 60 + mi


def solve():
	t = int(input())
	for x in range(t):
		T = int(input())
		na, nb = map(int, input().split())
		trains_a = []
		trains_b = []
		for _ in range(na):
			fa, tb = map(str, input().split())
			trains_a.append((convert_int(fa), convert_int(tb), 0))

		for _ in range(nb):
			fb, ta = map(str, input().split())
			trains_b.append((convert_int(fb), convert_int(ta), 1))

		trains = (trains_a + trains_b)
		#trains.sort(key = lambda x: x[0])
		trains.sort(key=compare_time)
		ans = train_time(trains, T)
		print("Case #%s: %s %s" % (x + 1, ans[0], ans[1]))


def compare_time(x: Tuple) -> int:
	return x[0]


solve()





