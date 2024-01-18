# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_inplace(self, llist):
        current = llist
        order = llist
        temp = None
        while current:
            order = order.next
            current.next = temp
            temp = current
            current = order
        return temp

    def get_mid(self, llist):
        slow = fast = llist
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head) -> bool:
        mid = self.get_mid(head)
        second_half = self.reverse_inplace(mid)

        pt1, pt2 = head, second_half
        while (pt1 and pt2) and (pt1.val == pt2.val):
            # print(pt1, pt2)
            pt1 = pt1.next
            pt2 = pt2.next

        return pt2 is None
