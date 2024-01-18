from collections import Counter

class Solution:
    """
    Time complexity -> O(max(S, T))
    Space complexity --> O(max(S, T))
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        for ch in s_count:
            if s_count[ch] != t_count[ch]:
                return False

        return True
