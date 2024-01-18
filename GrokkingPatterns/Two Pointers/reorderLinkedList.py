# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverse(self, head_node):
        current = head_node
        next_in = head_node
        temp = None
        while current is not None:
            next_in = next_in.next
            current.next = temp
            temp = current
            current = next_in
        return temp

    def get_mid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid_node = self.get_mid(head)
        second_half = self.reverse(mid_node)
        curr = head
        pt2 = second_half
        pt2_order = second_half
        while pt2 is not None:
            pt2_order = pt2_order.next
            hold = curr.next
            curr.next = pt2
            curr = pt2
            curr.next = hold
            curr = curr.next
            pt2 = pt2_order

        if curr:
            curr.next = None