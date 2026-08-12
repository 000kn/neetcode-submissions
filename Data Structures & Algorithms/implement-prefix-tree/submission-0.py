class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isLeaf = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.child[index] is None:
                cur.child[index] = TrieNode()
            cur = cur.child[index]
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.child[index] is None:
                return False
            cur = cur.child[index]
        return cur.isLeaf

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if cur.child[index] is None:
                return False
            cur = cur.child[index]
        return True