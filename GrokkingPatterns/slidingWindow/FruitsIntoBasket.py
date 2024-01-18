import collections


class Solution:
    def totalFruit(self, fruits: [int]) -> int:
        s = fruits
        start = 0
        ans = 0
        window = collections.defaultdict(int)
        for end in range(len(s)):
            window[s[end]] += 1
            while len(window) > 2:
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                start += 1

            ans = max(ans, end - start + 1)

        return ans