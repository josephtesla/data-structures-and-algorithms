class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for k in range(len(s)):
            i = j = k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1

            i = k
            j = k + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1

        return ans



