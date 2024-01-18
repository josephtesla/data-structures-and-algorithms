from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        ans = 1
        windowCount = defaultdict(int)
        for end in range(len(s)):
            # Find a valid window
            # Update max len
            char = s[end]
            windowCount[char] += 1
            # check window
            while end - start + 1 - max(windowCount.values()) > k:
                windowCount[s[start]] -= 1
                start += 1

            ans = max(ans, end - start + 1)

        return ans


print(Solution().characterReplacement("AABABBA", 1))






