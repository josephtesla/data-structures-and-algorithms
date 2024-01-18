class DLLNode:
    def __init__(self, data, key=None):
        self.val = data
        self.prev = None
        self.next = None
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys_map = dict()
        self.count = 0

        self.start = DLLNode(0)
        self.last = DLLNode(0)
        self.start.next = self.last
        self.last.prev = self.start

    def insert_start(self, node):
        start_next = self.start.next
        self.start.next = node
        node.prev = self.start
        node.next = start_next
        start_next.prev = node

    def delete_node(self, node):
        temp_prev = node.prev
        temp_next = node.next
        temp_prev.next = temp_next
        temp_next.prev = temp_prev

    def get(self, key: int) -> int:
        # print("getting ", key)
        if key not in self.keys_map:
            return -1

        node = self.keys_map[key]
        self.delete_node(node)
        self.insert_start(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # print("putting", key, value)
        new_node = DLLNode(value, key)

        if key in self.keys_map:
            present_node = self.keys_map[key]
            self.delete_node(present_node)
            self.insert_start(new_node)
            self.keys_map[key] = new_node
            return

        self.insert_start(new_node)
        self.keys_map[key] = new_node
        if self.count + 1 > self.capacity:
            # evict last node
            last_node = self.last.prev
            # print(last_node.val, last_node.key)
            self.delete_node(last_node)
            del self.keys_map[last_node.key]
        else:
            self.count += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
