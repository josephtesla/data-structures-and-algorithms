from collections import defaultdict


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return k
        ans = 0
        start, window_count = 0, defaultdict(int)
        for end in range(len(s)):
            window_count[s[end]] += 1
            while len(window_count) > k:
                # shrink
                print(start)
                window_count[s[start]] -= 1
                if window_count[s[start]] == 0:
                    del window_count[s[start]]
                start += 1
            ans = max(ans, end - start + 1)

        return ans


print(Solution().lengthOfLongestSubstringKDistinct("eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh", 16))
