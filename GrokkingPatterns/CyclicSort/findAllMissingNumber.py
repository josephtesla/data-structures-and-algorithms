class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        i = 0
        result = []
        while i < len(nums):
            j = nums[i] - 1
            if i != j and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            val = nums[i]
            if i + 1 != val:
                result.append(i + 1)

        return result
