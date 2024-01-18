"""
Time Complexity -> O(n)
Space Complexity --> O(1)
"""

class Solution:
    def maxProduct(self, nums: [int]) -> int:
        ans = max(nums)

        currentMaxProduct = nums[0]
        currentMinProduct = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num == 0:
                currentMaxProduct = 1
                currentMinProduct = 1
                continue

            temp_max = currentMaxProduct * num
            temp_min = currentMinProduct * num

            currentMaxProduct = max(temp_max, temp_min, num)
            currentMinProduct = min(temp_max, temp_min, num)

            ans = max(ans, currentMaxProduct)

        return ans




