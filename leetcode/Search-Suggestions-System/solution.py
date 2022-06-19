class Solution:
    def __init__(self):
        self.head = Node(None)
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        
        for product in products:
            current_node = self.head
            for alpha in product:
                if alpha not in current_node.children:
                    current_node.children[alpha] = Node(alpha)
                    current_node.children[alpha].data.append(product)
                else:
                    current_node.children[alpha].data.append(product)
                current_node = current_node.children[alpha]
        
        result = []
        current_node = self.head
        for alpha in searchWord:
            if alpha in current_node.children:
                if len(current_node.children[alpha].data) > 3:
                    result.append(current_node.children[alpha].data[:3])
                else:
                    result.append(current_node.children[alpha].data)
                current_node = current_node.children[alpha]
            else:
                result.append([])
                current_node.children[alpha] = Node(None)
                current_node = current_node.children[alpha]
        return result
        
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = []
        self.children = {}