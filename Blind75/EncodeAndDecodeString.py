class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        print(str)
        res = []
        i = 0
        current_len = ""
        getting_str = False
        while i < len(str):
            if not getting_str:
                if str[i].isdigit():
                    current_len += str[i]

                if str[i] == "#":
                    getting_str = True
            else:
                res.append(str[i: i + int(current_len)])
                getting_str = False
                i = i + int(current_len)
                current_len = ""
                continue

            i += 1

        return res
