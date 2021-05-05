"""
Climbing Stairs - How many ways to climb
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""
class Solution:
    """
    Approach: Recursion + Memoization
    Time Complexity = O(N) - Size of recursion tree can go upto n
    Space Complexity = O(n) - The depth of recursion tree can go upto n
    """
    def climbStairs(self, n: int) -> int:
        memo={}
        def recur_Climb(n):
            if n in memo:
                return memo[n]
            elif not n or n == 1:
                return 1
            else:
                result = recur_Climb(n-1)+recur_Climb(n-2)
            memo[n]= result
            return result 
        return recur_Climb(n)
