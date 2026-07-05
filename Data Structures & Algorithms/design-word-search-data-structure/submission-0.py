class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        return self.search2(self.root, word)

    def search2(self, root, word: str) -> bool:
        curr = root
        for i, c in enumerate(word):
            if c == '.':
                temp = curr
                for key in curr.child.keys():
                    curr = temp.child[key]
                    if self.search2(curr, word[i+1:]):
                        return True
            
            if c not in curr.child:
                return False
            curr = curr.child[c]
        
        return True if curr.end else False
        
class Node:
    def __init__(self):
        self.child = {}
        self.end = False