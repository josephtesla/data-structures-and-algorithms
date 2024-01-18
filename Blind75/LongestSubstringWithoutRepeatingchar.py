from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ans = 0
        positions = defaultdict(int)
        for end in range(len(s)):
            char = s[end]
            if char in positions:
                start = max(start, positions[char] + 1)

            positions[char] = end
            ans = max(ans, end - start + 1)

        return ans


print(Solution().lengthOfLongestSubstring("abba"))