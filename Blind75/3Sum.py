class Solution:
    def threeSum(self, nums: [int], target=0) -> [[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        results = []
        for i in range(n):
            element = nums[i]

            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                currentSum = element + nums[left] + nums[right]
                if currentSum == target:
                    # print(i, left, right)
                    # print(element, nums[left], nums[right])
                    results.append([element, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif currentSum < target:
                    left += 1
                else:
                    right -= 1

        return results


print(Solution().threeSum([-1,0,1,2,-1,-4]))




