class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:

        low = 0
        high = len(nums) - 1
        while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
            low += 1

        if low == len(nums) - 1:
            return 0

        while high > 0 and nums[high] >= nums[high - 1]:
            high -= 1

        max_num = max(nums[low: high + 1])
        min_num = min(nums[low: high + 1])

        while low > 0 and nums[low - 1] > min_num:
            low -= 1

        while high < len(nums) - 1 and nums[high + 1] < max_num:
            high += 1

        return high - low + 1