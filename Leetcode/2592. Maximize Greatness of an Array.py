"""
You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.
We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].
Return the maximum possible greatness you can achieve after permuting nums.

Example 1:
Input: nums = [1,3,5,2,1,3,1]
Output: 4
Explanation: One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.
"""
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        """
        1. Sort the input array 
        2.  For each element it , check if it > nums[ans]
        => If true, it means there still be 1 vale > than nums[ans], increase ans to check the next idx
        Time: O(nlog) due to sorting
        Space: O(1)
        """
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            if nums[i] > nums[ans]:
                ans += 1
        return ans
