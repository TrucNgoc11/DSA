class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        s = s.lstrip()
        positive = True
        if len(s) == 0:
            return res
        if s[0] == "+":
            positive = True
            s = s.lstrip("+")
        else:
            positive = False
            s = s.lstrip("-")
        for c in s:
            if not c.isdigit():
                if positive:
                    return min(2 ** 31 - 1, res)
                else:
                    return max(-2 ** 31 - 1, res * -1)

            res = res * 10 + (c - "0")
            print(c, c - "0")



