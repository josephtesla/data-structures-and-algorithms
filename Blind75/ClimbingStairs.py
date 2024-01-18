class Solution:
    """
    O(N) with memoization
    O(2^N) with normal bruteforce
    """
    def climbStairs(self, n: int) -> int:
        def solve(n, memo={}):
            if n in memo:
                return memo[n]

            if n <= 2:
                return n

            memo[n] = solve(n - 1) + solve(n - 2)

            return memo[n]
        return solve(n)
