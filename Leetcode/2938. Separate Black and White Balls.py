"""
2938. Separate Black and White Balls
There are n balls on a table, each ball has a color black or white.
You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
In each step, you can choose two adjacent balls and swap them.
Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

Example 1:
Input: s = "101"
Output: 1
Explanation: We can group all the black balls to the right in the following way:
- Swap s[0] and s[1], s = "011".
Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.
"""
class Solution:
    def minimumSteps(self, s: str) -> int:
        return self.v1(s)

    def v2(self, s):
        """
        two adjacent balls: Hai qua bong lien ke
        1. Count the nums of 1 appear and save the index
        2. With each position of 1, have to take n - i - 1 - index to the end of string
        Time: O(n)
        Space: O(1)
        """
        n = len(s)
        count_1 = []
        ans = 0
        for i in range(n):
            if s[i] == "1":
                count_1.append(i)
        
        for i in range(len(count_1)):
            ans += (n - i - count_1[i] - 1)
        return ans

    def v1(self, s):
        """
        1. start from the end of string
        2. With each 0, count + 1
        3. With each 1, ans increase by the nums of zero have found because 1 shoud be place to the right of string
        Time: O(n)
        Space: O(1)

        """
        n = len(s)
        ans, count = 0, 0
        for j in range(n - 1, -1, -1):
            if s[j] == "0":
                count += 1
            else:
                ans += count
        return ans




        
        
        
        
        
