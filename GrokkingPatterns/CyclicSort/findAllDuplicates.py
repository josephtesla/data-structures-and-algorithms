class Solution:
    def findDuplicates(self, nums: [int]) -> [int]:
        i = 0
        result = []
        while i < len(nums):
            j = nums[i] - 1
            print(i, nums, j)
            if i != j and nums[i] >= 0:
                if nums[j] == nums[i]:
                    result.append(nums[i])
                    nums[i], nums[j] = -1 * nums[i], -1 * nums[j]
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        return result

print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
