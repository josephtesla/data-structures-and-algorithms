# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        fast = slow = head
        exists = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                exists = True
                break

        if exists:
            p, q = head, fast
            while p and q:
                if p == q:
                    return p

                p = p.next
                q = q.next

        return None

#         pos = -1
#         seen_pos = dict()
#         curr = head
#         while curr is not None:
#             pos += 1
#             if curr in seen_pos:
#                 return curr

#             seen_pos[curr] = pos
#             curr = curr.next

#         return None
