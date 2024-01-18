from collections import deque


def binary_search(array, low, high, element):
    if low >= high:
        return -1

    mid = (low + high) // 2
    if array[mid] < element:
        return binary_search(array, low + 1, high, element)
    elif array[mid] == element:
        return mid
    else:
        return binary_search(array, low, high - 1, element)


# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            # and swap with current element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


#
# # Driver code to test above
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("Sorted array is:")
# print(arr)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]

        current.isEndOfWord = True

    def search(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]

        return current.isEndOfWord

    def starts_with(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return True


def inOrder(root):
    if not root:
        return

    inOrder(root.left)
    print(root.data, end="----")
    inOrder(root.right)


def inOrderItr(root):
    stack = []
    current = root
    while True:
        if current is not None:
            # Go Leftmost first
            stack.append(current)
            current = current.left

        elif len(stack) != 0:
            # get last pushed node
            current = stack.pop()
            print("current node -> ", current.data)
            current = current.right

        else:
            # End traversal
            break


def preOrderItr(root):
    stack = []
    current = root
    while True:
        if current is not None:
            print("current node -> ", current.data)
            # Go Left
            stack.append(current)
            current = current.left

        elif len(stack) != 0:
            # get last pushed node
            current = stack.pop()
            # go right
            current = current.right

        else:
            # End traversal
            break


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def printGraph(self):
        for u, neighbors in self.graph.items():
            print('{} ({})'.format(u, neighbors))

    def DFS(self, s):

        # mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # create a stack for DFS
        stack = []

        # Mark the source node as visited and push to stack
        stack.append(s)

        while len(stack) != 0:
            # pop the last added vertex from the stack and print it
            s = stack.pop()

            # mark as visited after popping from stack
            if not visited[s]:
                visited[s] = True
                print(s)

            # get all adjacent vertices of the popped vertex s
            # if an adjacent has not being visited/discovered,
            for u in self.graph[s]:
                if visited[u] == False:
                    stack.append(u)

    def DFSrecursive(self, s):
        visited = [False] * (max(self.graph) + 1)

        def dfs(node):
            nonlocal visited
            visited[node] = True
            print(node)
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        dfs(s)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


# g.printGraph()
#
# print("Following is Breadth First Traversal (starting from vertex 2)")
# g.DFSrecursive(2)

# traverse a matrix with dfs


def traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for move in moves:
            next_i, next_j = i + move[0], j + move[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:  # boundary
                dfs(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            dfs(i, j)
