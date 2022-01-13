# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftOrderTraverse(self, child):
        temp_list = []
        if child == None:
            temp_list.extend(["null"])
        elif child.left != None and child.right != None:
            temp_list.extend([child.val])
            temp_list.extend(self.leftOrderTraverse(child.left))
            temp_list.extend(self.leftOrderTraverse(child.right))
        elif child.left != None and child.right == None:
            temp_list.extend([child.val])
            temp_list.extend(self.leftOrderTraverse(child.left))
            temp_list.extend(["null"])
        elif child.left == None and child.right != None:
            temp_list.extend([child.val])
            temp_list.extend(["null"])
            temp_list.extend(self.leftOrderTraverse(child.right))
        else: #child.left == None and child.right == None:
            temp_list.extend([child.val])
        
        return temp_list
    
    def rightOrderTraverse(self, child):
        temp_list = []
        
        if child == None:
            temp_list.extend(["null"])
        elif child.left != None and child.right != None:
            temp_list.extend([child.val])
            temp_list.extend(self.rightOrderTraverse(child.right))
            temp_list.extend(self.rightOrderTraverse(child.left))
        elif child.left != None and child.right == None:
            temp_list.extend([child.val])
            temp_list.extend(["null"])
            temp_list.extend(self.rightOrderTraverse(child.left))
        elif child.left == None and child.right != None:
            temp_list.extend([child.val])
            temp_list.extend(self.rightOrderTraverse(child.right))
            temp_list.extend(["null"])
        else: #child.left == None and child.right == None:
            temp_list.extend([child.val])
        
        return temp_list
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left_list = self.leftOrderTraverse(root.left)
        right_list = self.rightOrderTraverse(root.right)
        for x,y in zip(left_list, right_list):
            if x != y:
                return False
        
        return True