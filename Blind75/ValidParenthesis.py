class Solution:

    # Time Complexity ---> O(N)
    # Space --> O(N)

    def isValid(self, s: str) -> bool:
        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for char in s:
            # if an opening
            if char in brackets:
                stack.append(char)
            else:
                # if a closing
                if len(stack) == 0:
                    return False
                else:
                    last = stack.pop()
                    if brackets[last] != char:
                        return False

        return len(stack) == 0
