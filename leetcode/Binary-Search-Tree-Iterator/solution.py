# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    val_list = []
    
    def inOrder(self, node):
        temp_list = []
        if node == None:
            return temp_list
        else:
            if node.left != None:
                temp_list.extend(self.inOrder(node.left))
            temp_list.append(node.val)
            if node.right != None:
                temp_list.extend(self.inOrder(node.right))
                
            return temp_list
    
    def __init__(self, root: Optional[TreeNode]):
        self.val_list = self.inOrder(root)

    def next(self) -> int:
        return self.val_list.pop(0)
    
    def hasNext(self) -> bool:
        if len(self.val_list) > 0:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()