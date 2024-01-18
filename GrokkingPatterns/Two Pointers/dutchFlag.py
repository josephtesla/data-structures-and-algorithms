def dutchFlag(array):
    low = 0
    high = len(array) - 1
    i = 0
    while i <= high:
        if array[i] == 0:
            array[i], array[low] = array[low], array[i]
            low += 1
            i += 1
        elif array[i] == 2:
            array[i], array[high] = array[high], array[i]
            high -= 1
        else:
            i += 1

    return array