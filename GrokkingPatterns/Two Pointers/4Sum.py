class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:

        nums.sort()
        result = []
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, len(nums)):
                if j - 1 > i and nums[j - 1] == nums[j]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif curr_sum < target:
                        left += 1

                    else:
                        right -= 1

        return result
