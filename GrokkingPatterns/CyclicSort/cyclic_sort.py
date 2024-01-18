class CyclicSort:
    @staticmethod
    def sort(nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            #print(nums)
            if j != i and nums[i] != nums[j]:
                # swap
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # corrupt pairs
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return [nums[i], i + 1]


nums = [3, 1, 2, 5, 2]

print(CyclicSort.sort(nums))
print(nums)
