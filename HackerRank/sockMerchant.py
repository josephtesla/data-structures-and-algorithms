from collections import defaultdict

def sockMerchant(n, ar):
    # Write your code here
    counter = defaultdict(int)
    ans = 0
    for color in ar:
        counter[color] += 1

    for color, count in counter.items():
        if count >= 2:
            ans += count // 2

    return ans
