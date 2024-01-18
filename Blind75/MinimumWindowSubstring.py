from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        subStr = ""
        subStrLen = float("inf")

        t_count = Counter(t)
        required_characters = len(t_count)
        formed_characters = 0
        windowCount = defaultdict(int)

        for end in range(len(s)):
            current_ch = s[end]
            windowCount[current_ch] += 1

            if current_ch in t_count and windowCount[current_ch] == t_count[current_ch]:
                formed_characters += 1

            while start <= end and formed_characters == required_characters:
                # Find a smaller window
                windowLength = end - start + 1
                if windowLength < subStrLen:
                    subStrLen = windowLength
                    subStr = s[start: end + 1]

                # find a smaller window
                if s[start] in t_count and (windowCount[s[start]] == t_count[s[start]]):
                    formed_characters -= 1

                windowCount[s[start]] -= 1
                start += 1

        return subStr


print(Solution().minWindow("ADOBECODEBANC", "ABC"))




# from collections import defaultdict, Counter
#
#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#
#         def isValidWindow(window, t_c):
#             for ch in t_c:
#                 if t_c[ch] > window[ch]:
#                     return False
#
#             return True
#
#         start = 0
#         subStr = ""
#         subStrLen = float("inf")
#
#         t_count = Counter(t)
#         windowCount = defaultdict(int)
#
#         for end in range(len(s)):
#             windowCount[s[end]] += 1
#             while isValidWindow(windowCount, t_count):
#                 windowLength = end - start + 1
#                 if windowLength < subStrLen:
#                     subStrLen = windowLength
#                     subStr = s[start: end + 1]
#
#                 # find a smaller window
#                 windowCount[s[start]] -= 1
#                 start += 1
#
#         return subStr
#
#
# print(Solution().minWindow("ADOBECODEBANC", "ABC"))
