

def check_pa(x: int):
	if x < 0:
		return False
	ori = x
	re = 0
	while x > 0:
		last_digit = x % 10
		re = 10 * re + last_digit
		x = x // 10
	return ori == re


def new(x: str, cnt: int):
	ans = ""
	while len(ans) < cnt:
		for i in range(len(x)):
			ans += x[i]
			if len(ans) == cnt:
				break
	return ans


def solve():
	t = int(input())
	for _ in range(t):
		num = int(input())
		cnt = 0
		for a in str(num):
			cnt += int(a)
		new_num = new(str(num), cnt)
		ans = check_pa(int(new_num))
		if ans:
			print("YES")
		else:
			print("NO")


solve()