def helper(expression):
	st = []
	ans = 0
	for i in range(len(expression)):
		if expression[i] == "<":
			st.append(expression[i])
		elif len(st) == 0:
			break
		else:
			st.pop()
			if len(st) == 0:
				ans = i + 1
	return ans


def solve():
	n = int(input())
	for _ in range(n):
		expression = input()
		print(helper(expression))


solve()
