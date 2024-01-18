from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node'):
        if node is None:
            return None

        clones = dict()

        def clone(current_node):
            if current_node in clones:
                return clones[current_node]

            clone_copy = Node(current_node.val)
            clones[current_node] = clone_copy

            for neighbor in current_node.neighbors:
                neighbor_clone = clone(neighbor)
                clone_copy.neighbors.append(neighbor_clone)

            return clone_copy

        return clone(node)
