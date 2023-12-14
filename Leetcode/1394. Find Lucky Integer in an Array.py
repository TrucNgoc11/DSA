"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
"""
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s = Counter(arr)
        ans = 0
        for val in arr:
            if val == s[val]:
                ans = max(ans, val)
        return ans if ans != 0 else -1
