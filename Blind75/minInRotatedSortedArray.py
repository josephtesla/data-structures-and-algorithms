"""
Time --> O(LOG N)
Space --> O(LOG N)
"""

class Solution:
    def findMin(self, arr:[int]) -> int:
        low = 0
        high = len(arr) - 1
        minimum = float("inf")
        while low <= high:
            mid = (low + high) // 2
            minimum = min(minimum, arr[mid])
            # if left array is sorted
            if arr[low] <= arr[mid]:
                minimum = min(minimum, arr[low])
                # continue on the right
                low = mid + 1

            else:
                minimum = min(minimum, arr[mid])
                # continue on the left
                high = mid - 1

        return minimum



