class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        LIS = [1] * (n + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    LIS[i] = max(1 + LIS[j], LIS[i])

        return max(LIS)
