# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reConnect(self, node):
        if node == None:
            return None
        else:
            left = None
            if node.left != None:
                left = self.reConnect(node.left)
                    
            right = None
            if node.right != None:
                right = self.reConnect(node.right)
                
            if left != None:
                # left node last connect
                curr = left
                while curr.right != None:
                    curr = curr.right
                curr.right = node
                
                if right != None:
                    node.right = right
                node.left = None
                return left
            elif left == None and right != None:
                node.right = right
                node.left = None
                return node
            else:
                return node
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        answer = self.reConnect(root)
        return answer