from collections import defaultdict


class Solution:
    def longestOnes(self, nums: [int], k: int) -> int:
        ans = 0
        start = 0
        window_count = defaultdict(int)
        for end in range(len(nums)):
            window_count[nums[end]] += 1
            while window_count[0] > k:
                window_count[nums[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)

        return ans
