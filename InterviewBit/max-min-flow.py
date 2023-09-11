class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #time complexity: O(n)
        #Space: O(1)
        total = max(A) + min(A)
        return total
