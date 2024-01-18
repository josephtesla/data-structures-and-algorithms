class Solution:

    # Time Complexity --> O(N)
    # Space --> O(N)

    def productExceptSelf(self, nums: [int]):
        n = len(nums)
        prefixProducts = [1] * n
        suffixProducts = [1] * n

        for i in range(1, n):
            prefixProducts[i] = prefixProducts[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffixProducts[i] = suffixProducts[i + 1] * nums[i + 1]

        return [suffixProducts[i] * prefixProducts[i] for i in range(n)]

