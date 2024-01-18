# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def get_length(self, head):
        ans = 0
        curr = head
        while curr:
            ans += 1
            curr = curr.next
        return ans

    def findNode(self, longer, shorter, diff):
        l_curr = longer
        s_curr = shorter
        for _ in range(diff):
            l_curr = l_curr.next

        while l_curr and s_curr:
            if l_curr == s_curr:
                return l_curr

            l_curr = l_curr.next
            s_curr = s_curr.next

        return None

    def getIntersectionNode(self, headA, headB):
        a_len = self.get_length(headA)
        b_len = self.get_length(headB)

        if a_len >= b_len:
            return self.findNode(headA, headB, a_len - b_len)
        else:
            return self.findNode(headB, headA, b_len - a_len)


