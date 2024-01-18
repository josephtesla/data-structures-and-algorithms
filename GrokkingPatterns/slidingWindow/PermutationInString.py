from collections import defaultdict, Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counter = Counter(s1)
        window_counter = defaultdict(int)
        formed = 0
        required = len(s1_counter)
        for i in range(len(s1)):
            window_counter[s2[i]] += 1
            if s2[i] in s1_counter and window_counter[s2[i]] == s1_counter[s2[i]]:
                formed += 1
            if formed == required:
                return True

        start = 0
        for end in range(len(s1), len(s2)):
            if s2[start] in s1_counter and s1_counter[s2[start]] == window_counter[s2[start]]:
                formed -= 1
            window_counter[s2[start]] -= 1
            start += 1

            window_counter[s2[end]] += 1
            if s2[end] in s1_counter and s1_counter[s2[end]] == window_counter[s2[end]]:
                formed += 1

            if formed == required:
                return True

        return False
