class WordFilter:

    def __init__(self, words: List[str]):
        self.head = Node(None)
        self.result_dict = {}
        
        for index, word in enumerate(words):
            current_node = self.head
            current_node.data.append((word, index))
            for alpha in word:
                if alpha not in current_node.children:
                    current_node.children[alpha] = Node(alpha)
                    
                current_node.children[alpha].data.append((word, index))
                current_node = current_node.children[alpha]

    def f(self, prefix: str, suffix: str) -> int:
        current_node = self.head
    
        if (prefix,suffix) in self.result_dict:
            return self.result_dict[(prefix,suffix)]
        
        for pre in prefix:
            if pre in current_node.children:
                current_node = current_node.children[pre]
            else:
                return -1
        # self.head.traverse()
        max_num = -1
        for word, index in current_node.data:
            if suffix == word[-len(suffix):]:
                if max_num < index:
                    max_num = index
        
        self.result_dict[(prefix,suffix)] = max_num
        return max_num

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = []
        self.children = {}
        
    def traverse(self):
        if len(self.children) == 0:
            print(self.data)
        else:
            for alpha in self.children:
                print(self.children[alpha].data)
                self.children[alpha].traverse();
    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)