class Node:
    def __init__(self):
        self.child = [None] * 26
        self.EOL = False


class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            i = ord(c) - ord('a')
            if curr.child[i] == None:
                curr.child[i] = Node()
            curr = curr.child[i]
        curr.EOL = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            i = ord(c) - ord('a')
            if curr.child[i] == None:
                return False
            curr = curr.child[i]
        return True if curr.EOL else False
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.child[i] == None:
                return False
            curr = curr.child[i]
        return True

        
        