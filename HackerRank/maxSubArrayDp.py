# Complete the maxSubsetSum function below.

# Complete the maxSubsetSum function below.
def maxSubsetSum2(arr):
    n = len(arr)
    dp = [arr[i] for i in range(len(arr))]

    # find max for each index using bottom-up dp
    for i in range(n - 3, -1, -1):
        current_maximum = dp[i]
        for j in range(i + 2, n):
            dp[i] = max(dp[i], current_maximum + dp[j])

    return max(dp)


def maxSubsetSum(arr):
    currentMaxSum = 0
    last_added_index = -1

    positiveExists = False

    for i in range(len(arr)):
        currentValue = arr[i]
        if currentValue > 0:
            positiveExists = True
            if i - 2 >= last_added_index:
                currentMaxSum += currentValue
                last_added_index = i
            else:
                if currentValue > arr[i - 1]:
                    currentMaxSum -= arr[i - 1]
                    currentMaxSum += currentValue
                    last_added_index = i

    if not positiveExists:
        return max(arr)

    return currentMaxSum


import math


def leftRotate(array, d):
    n = len(array)
    results = [-1] * n

    for i in range(n):
        new_position = i - d
        if new_position < 0:
            new_position = math.ceil(abs(new_position / n)) * n + new_position
        results[new_position] = array[i]

    return results

def rotateRight(array, d):
    n = len(array)
    results = [-1] * n

    for i in range(n):
        new_position = i + d
        if new_position > n - 1:
            new_position = new_position % n
        results[new_position] = array[i]

    return results

print(rotateRight([1,2,3,4,5], 9))