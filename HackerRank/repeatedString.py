def repeatedString(s, n):
    # Write your code here
    no_of_a = s.count("a")
    possible_strings_count = n // len(s)
    remaining_str_count = n % len(s)

    ans = no_of_a * possible_strings_count
    ans += s[0: remaining_str_count].count("a")

    return ans
