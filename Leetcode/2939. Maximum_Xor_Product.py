"""
Given three integers a, b, and n, return the maximum value of (a XOR x) * (b XOR x) where 0 <= x < 2n.

Since the answer may be too large, return it modulo 109 + 7.

Note that XOR is the bitwise XOR operation.
Example 1:
Input: a = 12, b = 5, n = 4
Output: 98
Explanation: For x = 2, (a XOR x) = 14 and (b XOR x) = 7. Hence, (a XOR x) * (b XOR x) = 98. 
It can be shown that 98 is the maximum value of (a XOR x) * (b XOR x) for all 0 <= x < 2n.
"""

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        """
        XOR is a bitwise opearation
        to maximize a x b
        1. a and b has 1 => x shoud have 0
        2. a and b has 0 => x shoud have 1
        3. a has 1, b has 1 or nguoc lai:
        + sum a + b  not change
        + but product of fix sum is maximized when a and b closer
        Ex: 5 + 5 = 2 + 8 but 5x5 > 2x8
        => so if a>b, set 1 in x to make them more equal
        otherwise, set 0 in x
        * 2 reasons why a>b:
         + a has some bit j > i and b does not have j => swap to make them closer
         + a has i and b does not have i. a and be have the same prefix. 
         => all less significant bits will go to the one that doesn't have bit i 
         (because it will always be less then the other)

        """
        MOD = 10** 9 + 7
        for i in reversed(range(n)):
            mask = 1 << i
            #a and b has 1 => x shoud have 0
            if (a & mask) and (b & mask):
                continue
            elif (a & mask):
                if a > b:
                    a ^= mask
                    b |= mask
            elif (b & mask):
                if a < b:
                    a |= mask
                    b ^= mask
            else:
                a |= mask
                b |= mask
        a %= MOD
        b %= MOD
        return (a * b) % MOD

        





        
