class Solution:
    """
    Time --> O(N)
    Space --> O(1)
    """
    def maxSubArray(self, nums: [int]) -> int:
        currentSum = nums[0]
        maxSum = currentSum
        for i in range(1, len(nums)):
            num = nums[i]
            currentSum = max(currentSum + num, num)
            maxSum = max(currentSum, maxSum)

        return maxSum

