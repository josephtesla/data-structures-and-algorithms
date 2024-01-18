class Solution:
    def hasCycle(self, head) -> bool:
        hset = set()
        current = head

        while current is not None:
            if current in hset:
                return True

            hset.add(current)
            current = current.next

        return False

class Solution:
    # using Floyd's algorithm
    def hasCycle2(self, head) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False