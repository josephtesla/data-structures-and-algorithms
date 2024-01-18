# Quick select instead of heap solution

def partition(array, low, high):

    pivot = array[high]
    smaller_i = (low - 1)

    for i in range(low, high):
        if array[i] <= pivot:
            smaller_i += 1
            array[smaller_i], array[i] = array[i], array[smaller_i]

    array[smaller_i + 1], array[high] = array[high], array[smaller_i + 1]
    return smaller_i + 1


def kthSmallestElement(array, k):
    low, high = 0, len(array) - 1
    while low <= high:
        partition_index = partition(array, low, high)

        if partition_index == k - 1:
            return array[partition_index]

        elif partition_index < k - 1:
            low = partition_index + 1

        else:
            high = partition_index - 1

    return -1


print(kthSmallestElement([44, 22, 6, 7, 4, 33, 2, 8]))

# 6, 7, 4, 2 -- 8
# 2 -- 7, 4, 6
# 2, 4, 6, 7