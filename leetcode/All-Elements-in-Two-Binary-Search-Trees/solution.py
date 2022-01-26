# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treePop(self, Node):
        if Node == None:
            return []
        if Node.left == None and Node.right == None:
            return [Node.val]
        else:
            temp_list = [Node.val]
            if Node.left != None:
                temp_list.extend(self.treePop(Node.left))
            if Node.right != None:
                temp_list.extend(self.treePop(Node.right))
                
            return temp_list
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        list1 = self.treePop(root1)
        list2 = self.treePop(root2)
        
        result = []
        result.extend(list1)
        result.extend(list2)
        
        result = list(sorted(result))
        
        return result