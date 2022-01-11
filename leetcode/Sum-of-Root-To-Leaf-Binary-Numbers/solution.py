# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binary2int(self, num_str):
        result = 0;
        num_str = num_str[::-1]
        for i, n in enumerate(num_str):
            result += (2**i)* int(n)
        return result;
    
    def return_childNode(self, node: Optional[TreeNode]):
        if node.left == None and node.right == None:
            return [str(node.val)]
        elif node.left == None and node.right != None:
            temp_list = []
            temp_list.extend(self.return_childNode(node.right))
            result = []
            for temp in temp_list:
                result.append(str(node.val)+str(temp))
            return result
        elif node.right == None and node.left != None:
            temp_list = []
            temp_list.extend(self.return_childNode(node.left))
            result = []
            for temp in temp_list:
                result.append(str(node.val)+str(temp))
            return result
        else:
            temp_list = []
            temp_list.extend(self.return_childNode(node.left))
            temp_list.extend(self.return_childNode(node.right))
            result = []
            for temp in temp_list:
                result.append(str(node.val)+str(temp))
            return result
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        add_num = 0
        temp_list = self.return_childNode(root)
        for temp in temp_list:
            add_num += self.binary2int(temp)
        
        return add_num