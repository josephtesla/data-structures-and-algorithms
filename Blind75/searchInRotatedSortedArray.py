"""
Time --> O(LOG N)
Space --> O(LOG N)
"""

class Solution:
    def search(self, nums: [int], target: int) -> int:
        def binarySearch(arr, left, right, key):

            if left > right:
                return -1

            mid = (left + right) // 2

            if arr[mid] == key:
                return mid

            # check if left subarray is sorted
            if arr[left] <= arr[mid]:

                # if num in the range
                if arr[left] <= key <= arr[mid]:
                    # continue search on the left
                    return binarySearch(arr, left, mid - 1, key)
                else:
                    # continue search on the right
                    return binarySearch(arr, mid + 1, right, key)

            # then right sub array will be sorted

            # if num in the range
            if arr[mid] <= key <= arr[right]:
                # continue search on the right
                return binarySearch(arr, mid + 1, right, key)
            else:
                # continue search on the left
                return binarySearch(arr, left, mid - 1, key)

        return binarySearch(nums, 0, len(nums) - 1, target)


