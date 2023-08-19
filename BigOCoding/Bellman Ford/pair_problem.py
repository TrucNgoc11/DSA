from typing import List
INF = 1e9

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def distance(p1: Point, p2: Point) -> float:
	x = p1.x - p2.x
	y = p1.y - p2.y
	return (x * x + y * y) ** 0.5


def brute_force(point_set: List[Point], left: int, right: int) -> int:
	min_dist = INF
	for i in range(left, right):
		for j in range(i + 1, right):
			min_dist = min(min_dist, distance(point_set[i], point_set[j]))
	return min_dist


def strip_closest(point_set: List[Point], left: int, right: int, mid: int, min_dist: float):
	point_mid = point_set[mid]
	splitted_point = []
	for i in range(left, right):
		if abs(point_set[i].x - point_mid.x) <= min_dist:
			splitted_point.append(point_set[i])
	splitted_point.sort(key = lambda p: p.y)

	smallest = INF
	l = len(splitted_point)
	for i in range(0, l):
		for j in range(i + 1, l):
			if not (splitted_point[j].y - splitted_point[i].y) < min_dist:
				break
			d = distance(splitted_point[i], splitted_point[j])
			smallest = min(smallest, d)
	return smallest


def closest_until(point_set: List[Point], left: int,  right: int) -> float:
	if right - left < 3:
		return brute_force(point_set, left, right)
	mid = (left + right) // 2
	dist_left = closest_until(point_set, left, mid)
	dist_right = closest_until(point_set, mid + 1, right)
	dist_min = min(dist_left, dist_right)
	return min(dist_min, strip_closest(point_set, left, right, mid, dist_min))


def solve():
	while True:
		n = int(input())
		if n == 0:
			break
		point_set = []
		for _ in range(n):
			x, y = map(float, input().split())
			point_set.append(Point(x, y))
		point_set.sort(key = lambda p: p.x)
		ans = closest_until(point_set, 0, n)
		if ans < 10000:
			print("%.4f" % ans)
		else:
			print("INFINITY")


solve()