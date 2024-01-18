"""
    Time ----> O(N)
    Space ------> O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        temp = None
        current = head
        following = head

        while current is not None:
            following = following.next

            current.next = temp
            temp = current
            current = following

        return temp

