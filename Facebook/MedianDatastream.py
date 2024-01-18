import math
# Add any extra import statements you may need here
from heapq import heapify, heappop, heappush


# Add any helper functions you may need here


class MedianStream:
    def __init__(self):
        self.lower = []
        self.upper = []

    def insert(self, num):
        if not self.upper:
            heappush(self.upper, num)
        else:
            min_val = self.upper[0]
            if min_val >= num:
                heappush(self.lower, -num)
            else:
                heappush(self.upper, num)

        # balance
        if len(self.lower) - len(self.upper) > 1:
            max_val = -heappop(self.lower)
            heappush(self.upper, max_val)
        if len(self.upper) - len(self.lower) > 1:
            min_val = heappop(self.upper)
            heappush(self.lower, -min_val)

    def get_median(self):
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.lower) < len(self.upper):
            return self.upper[0]
        else:
            max_val = -self.lower[0]
            min_val = self.upper[0]
            return (min_val + max_val) // 2


def findMedian(arr):
    # Write your code here
    stream = MedianStream()
    output = [0] * len(arr)
    for i in range(len(arr)):
        stream.insert(arr[i])
        if i < 1:
            output[i] = arr[i]
        else:
            output[i] = stream.get_median()

    return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [5, 15, 1, 3]
    expected_1 = [5, 10, 5, 4]
    output_1 = findMedian(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [2, 3, 4, 3, 4, 3]
    output_2 = findMedian(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
