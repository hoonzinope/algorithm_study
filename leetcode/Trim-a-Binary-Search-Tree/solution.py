# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reconnect(self, node, low, high):
        if node == None:
            return None
        else:
            left = None
            if node.left != None:
                left = self.reconnect(node.left, low, high)
                                    
            right = None
            if node.right != None:
                right = self.reconnect(node.right, low, high)
            
            if node.val > high:
                if left != None and low <= left.val and left.val <= high:
                    return left
                else:
                    return None
            elif node.val < low:
                if right != None and low <= right.val and right.val <= high:
                    return right
                else:
                    return None
            else:
                if left == None:
                    node.left = None
                else:
                    node.left = left
                    
                if right == None:
                    node.right = None
                else:
                    node.right = right
                
                return node
            
            
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        answer = self.reconnect(root, low, high)
        return answer