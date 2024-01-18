"""
Without memoization: O(2^N)
With Memo: O(N x S) ---> where N is total number of elements, S is sum of elements
because we can only perform at most N X S operations since we using DP memo to cache results at each stage
"""

class Solution:
    def canPartition(self, nums: [int]) -> bool:
        nums_total = sum(nums)
        if nums_total % 2 != 0:
            return False

        half_sum = nums_total // 2

        print(half_sum, len(nums))
        dp = [[None] * (half_sum + 1) for _ in range(len(nums) + 1)]

        def sum_exists(nums, summ, current_index):
            if dp[current_index][summ] != None:
                return dp[current_index][summ]

            if summ == 0:
                return True

            if (len(nums) == 0 or current_index >= len(nums)):
                return False

            if (nums[current_index] <= summ):
                if sum_exists(nums, summ - nums[current_index], current_index + 1):
                    dp[current_index][summ] = True
                    return True

            dp[current_index][summ] = sum_exists(nums, summ, current_index + 1)
            return dp[current_index][summ]

        return sum_exists(nums, half_sum, 0)
