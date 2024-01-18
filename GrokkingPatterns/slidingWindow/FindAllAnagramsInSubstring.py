from collections import defaultdict, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        result = []

        if len(p) > len(s):
            return result

        p_count = Counter(p)
        window_count = defaultdict(int)
        required_chars = len(p_count)
        formed_chars = 0
        start = 0

        for i in range(len(p)):
            window_count[s[i]] += 1
            if s[i] in p_count and p_count[s[i]] == window_count[s[i]]:
                formed_chars += 1
            if formed_chars == required_chars:
                result.append(start)

        for end in range(len(p), len(s)):
            curr_start = s[start]
            # shift start
            if curr_start in p_count and window_count[curr_start] == p_count[curr_start]:
                formed_chars -= 1

            start += 1
            window_count[curr_start] -= 1

            # add end
            window_count[s[end]] += 1
            if s[end] in p_count and window_count[s[end]] == p_count[s[end]]:
                formed_chars += 1

            if formed_chars == required_chars:
                result.append(start)

        return result
