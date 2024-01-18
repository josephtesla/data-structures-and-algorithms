class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        currents = [self.root]
        for char in word:
            valid_nexts = []
            for current in currents:
                if char == ".":
                    valid_nexts += list(current.children.values())
                elif char in current.children:
                    valid_nexts.append(current.children[char])

            currents = valid_nexts
            if len(valid_nexts) == 0: return False

        for c in currents:
            if c.is_end_of_word: return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)