from collections import defaultdict

"""
    Time Complexity --> 
    Let N be total strings and S be average length of a string
    TC -> N * (SlogS)
"""


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        hashmap = defaultdict(list)
        result = []
        for word in strs:
            sortedWord = "".join(sorted(list(word)))
            hashmap[sortedWord].append(word)

        for array in hashmap.values():
            result.append(array)

        return result
