class Solution:
    def numSubarrayProductLessThanK(self, nums: [int], k: int) -> int:
        curr_product = 1
        ans = 0
        start = 0
        for i in range(len(nums)):
            curr_product *= nums[i]
            while curr_product >= k and start < len(nums):
                curr_product = curr_product // nums[start]
                start += 1

            if start == len(nums):
                break

            ans += i - start + 1

        return ans
