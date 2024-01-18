class Solution:
    """
    O(N^2) Complexity
    """
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort()
        min_diff = float("inf")
        ans = None
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right] + nums[i]
                diff = abs(target - curr_sum)
                if diff < min_diff:
                    min_diff = diff
                    ans = curr_sum

                if curr_sum <= target:
                    left += 1
                else:
                    right -= 1

        return ans


