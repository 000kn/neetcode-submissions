class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.child[index] is None:
                cur.child[index] = TrieNode()
            cur = cur.child[index]
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.child:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    index = ord(c) - ord('a')
                    if cur.child[index] is None:
                        return False
                    cur = cur.child[index]
            return cur.isLeaf
        return dfs(0, self.root)
