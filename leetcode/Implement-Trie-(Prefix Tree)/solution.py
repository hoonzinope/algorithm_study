class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        current_node = self.head
        for w in word:
            if w not in current_node.children:
                current_node.children[w] = Node()
            current_node = current_node.children[w]
        current_node.data.append(word)
        
    def search(self, word: str) -> bool:
        current_node = self.head
        for w in word:
            if w not in current_node.children:
                return False
            else:
                current_node = current_node.children[w]
        if word in current_node.data:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.head
        for w in prefix:
            if w not in current_node.children:
                return False
            else:
                current_node = current_node.children[w]
        if len(current_node.children) > 0 or len(current_node.data) > 0:
            return True
        else:
            return False

class Node:
    def __init__(self):
        self.data = []
        self.children = {}
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)