class Solution:
    # Time Complexity ---> O(n)
    # space complexity ---> O(n)

    def containsDuplicate(self, nums):
        seenElements = set()
        for element in nums:
            if element in seenElements:
                return True

            seenElements.add(element)

        return False
