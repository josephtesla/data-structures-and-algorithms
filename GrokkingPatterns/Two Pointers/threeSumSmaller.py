class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """

    def threeSumSmaller(self, nums, target):
        # Write your code here
        nums.sort()
        min_diff = float("inf")
        ans = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right] + nums[i]
                if curr_sum < target:
                    ans += right - left
                    left += 1
                else:
                    right -= 1

        return ans
