import collections
from typing import List

def solve():
	n = int(input())
	for _ in range(n - 1):
		a, b = map(int, input().split())
		gr = collections.defaultdict(list)
		gr[a].append(b)
	visited = [False] * n
	arr_time = [0] * n
	depth = [0] * n
	time = 1
	for i in range(n):
		if not visited[i]:
			dfs(i, gr, depth, time, arr_time, visited)

	k = int(input())
	for i in range(k):
		type, des, start = map(int, input().split())
		if type == 0:
			if arr_time[start - 1] > arr_time[des - 1] and depth[start - 1] < depth[des - 1]:
				print("YES")
			else:
				print("NO")
		else:
			if arr_time[start - 1] < arr_time[des - 1] and depth[start - 1] > depth[des - 1]:
				print("YES")
			else:
				print("NO")


def dfs(cur_node: int, graph: List[int], depth: int, time: int, arr_time: int, visited: List[bool]):
	visited[cur_node] = True
	arr_time[cur_node] = time
	time += 1
	for ne in graph[cur_node]:
		if not visited[ne]:
			dfs(ne, graph, depth, time, arr_time, visited)
	depth[cur_node] = time
	time += 1



solve()