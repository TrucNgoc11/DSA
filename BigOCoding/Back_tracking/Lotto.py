def bk(idx, arr, cur_list, ans):
	if len(cur_list) == 6: # generate all cases
		ans.append(list(cur_list))
		return
	if idx >= len(arr):
		return

	# pick
	cur_list.append(arr[idx])
	bk(idx + 1, arr, cur_list, ans)
	cur_list.pop()

	#no pick
	bk(idx + 1, arr, cur_list, ans)


def solve():
	while 1 == 1:
		t = list(map(int, input().split()))
		n, num_list = t[0], t[1:]
		if n == 0:
			break
		ans = []
		cur_list = []
		bk(0, num_list, cur_list, ans)
		for t in ans:
			print(" ".join(str(x) for x in t))
		print()




solve()
