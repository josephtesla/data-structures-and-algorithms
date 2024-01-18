class Solution:
    """
    O(N) time complexity
    space complexity -> O(1)
    we basically visit the array twice at worst case
    """
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        ans, n = float("inf"), len(nums)
        window_start = 0
        current_sum = 0
        for window_end in range(n):
            current_sum += nums[window_end]
            while current_sum >= target:
                # find a smaller window
                ans = min(ans, window_end - window_start + 1)
                current_sum -= nums[window_start]
                window_start += 1

        return ans if ans != float("inf") else 0
