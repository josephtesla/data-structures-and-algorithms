class Solution:
    def getString(self, s):
        backspace = 0
        s_final = []
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == "#":
                backspace += 1
            else:
                if backspace != 0:
                    backspace -= 1
                    continue
                else:
                    s_final.append(ch)

        return "".join(s_final)

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_final = self.getString(s)
        t_final = self.getString(t)
        return s_final == t_final

    def backspaceCompare_Optimal(self, s, t) -> bool:
        s_ptr, t_ptr = len(s) - 1, len(t) - 1
        while s_ptr >= 0 or t_ptr >= 0:
            s_ptr_next = self.get_next_valid_char(s, s_ptr)
            t_ptr_next = self.get_next_valid_char(t, t_ptr)
            print(s_ptr_next, t_ptr_next)

            if s_ptr_next < 0 and t_ptr_next < 0:
                return True

            elif s_ptr_next < 0 or t_ptr_next < 0:
                return False

            if s[s_ptr_next] != t[t_ptr_next]:
                return False

            s_ptr = s_ptr_next - 1
            t_ptr = t_ptr_next - 1

        return True

    def get_next_valid_char(self, string, index):
        backspace_count = 0
        i = index
        while i >= 0:
            if string[i] == "#":
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break

            i -= 1
        return i

