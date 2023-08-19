from collections import deque

def move_paper(a, ori, new, tab):
	a = ori.popleft()
	if a < 




def solve():
	t = int(input())
	for _ in range(t):
		ori_box = deque()
		n = int(input())
		for i in range(n):
			ori_box.append(i + 1)
		new_box = []
		table = deque()
		swa