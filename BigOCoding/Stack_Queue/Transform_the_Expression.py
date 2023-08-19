
def helper(expression):
	st = []
	for text in expression:
		if text.isalpha(): #check xem phai chuoi ki tu ko co khoang cach ko
			print(text, end ="")
		elif text == ")":
			print(st.pop(), end ="")
		elif text != "(":
			st.append(text)
	print()


def solve():
	test_case = int(input())
	for _ in range(test_case):
		expression = input()
		helper(expression)


solve()
