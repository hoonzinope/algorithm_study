# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        curr = root
        if curr == None:
            root = TreeNode(val=val)
            return root
        
        while curr != None:
            if curr.val < val:
                if curr.right != None:
                    curr = curr.right
                else:
                    break
            else:
                if curr.left != None:
                    curr = curr.left
                else:
                    break
                
            if curr.left == None and curr.right == None:
                break
                
        if curr.val > val:
            curr.left = TreeNode(val=val)
        else:
            curr.right = TreeNode(val=val)
        
        return root