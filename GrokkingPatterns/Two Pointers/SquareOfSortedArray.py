class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        negatives = []
        positives = []

        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)

        print(negatives, positives)

        # two pointers
        # merge the sorted lists
        result = []
        i = len(negatives) - 1
        j = 0
        while i >= 0 or j < len(positives):
            if i < 0 and j < len(positives):
                result.append(positives[j] ** 2)
                j += 1

            elif i >= 0 and j >= len(positives):
                result.append(negatives[i] ** 2)
                i -= 1

            else:
                if abs(negatives[i]) <= positives[j]:
                    result.append(negatives[i] ** 2)
                    i -= 1
                else:
                    result.append(positives[j] ** 2)
                    j += 1

        return result
