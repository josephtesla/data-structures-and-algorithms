class Solution:
    def twoSum(self, nums, target: int):

        # Time complexity = O(n)
        # Space Complexity = O(n)
        indices = {}
        for i in range(len(nums)):
            element = nums[i]
            remainder = target - element
            if remainder in indices:
                return [i, indices[remainder]]

            indices[element] = i

        return [-1, -1]