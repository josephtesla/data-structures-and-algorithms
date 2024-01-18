"""
Time Complexity --> O(N)
Space Complexity --> O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestPalindrome = s[0]
        maxLength = 1

        def findLongestFrom(i, j) -> (int, str):
            length = 1
            palindrome = s[i]
            while i >= 0 and j < len(s) and s[i] == s[j]:
                length = j - i + 1
                palindrome = s[i: j + 1]
                i -= 1
                j += 1

            return length, palindrome

        for k in range(len(s)):
            L, P = findLongestFrom(k, k)
            if L > maxLength:
                maxLength = L
                longestPalindrome = P

            L, P = findLongestFrom(k, k + 1)
            if L > maxLength:
                maxLength = L
                longestPalindrome = P

        return longestPalindrome


print(Solution().longestPalindrome("cbbd"))