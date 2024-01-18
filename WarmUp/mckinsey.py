def countHighlyProfitableMonths(stockPrices, k):
    # Write your code here
    ans = 0
    current = 1
    stockPrices.append(float('-inf'))
    for i in range(1, len(stockPrices)):
        if stockPrices[i - 1] < stockPrices[i]:
            current += 1
        else:
            if current >= k:
                ans += current - k + 1
            current = 1
    return ans

print(countHighlyProfitableMonths([5,3,5,7,8], 3))