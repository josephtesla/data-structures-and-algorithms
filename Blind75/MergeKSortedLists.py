from heapq import heappush, heappop, heapify


def mergeKSortedArrays(arrays):
    heap_ds = []
    for i in range(len(arrays)):
        array = arrays[i]
        # push  --> (value, [index in its array, index of its array])
        heappush(heap_ds, (array[0], [0, i]))

    result = []
    while heap_ds:
        next_smallest = heappop(heap_ds)
        value = next_smallest[0]
        index = next_smallest[1][0]
        arr_index = next_smallest[1][1]

        result.append(value)

        # push next value in its array to heap
        if index + 1 < len(arrays[arr_index]):
            heappush(heap_ds, (arrays[arr_index][index + 1], [index + 1, arr_index]))

    return result


print(mergeKSortedArrays([[1, 4, 5], [1, 3, 4], [2, 6]]))

from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
k * log k complexity
"""


class Solution:
    def mergeKLists(self, lists):
        heap_ds = []
        for linked_list_head in lists:
            if linked_list_head:
                heappush(heap_ds, (linked_list_head.val, linked_list_head))

        curr = result = ListNode(0)
        while heap_ds:
            next_smallest = heappop(heap_ds)
            value = next_smallest[0]
            node = next_smallest[1]
            curr.next = node
            curr = curr.next

            if node.next:
                pass
        heappush(heap_ds, (node.next.val, node.next))

        return result.next
