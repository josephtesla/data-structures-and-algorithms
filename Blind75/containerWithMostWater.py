"""
Time Complexity --> O(N)
Space ---> O(1)
"""

class Solution:
    def maxArea(self, height: [int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = float("-inf")
        while left <= right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


