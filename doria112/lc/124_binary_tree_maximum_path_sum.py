# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # tree postorder traversal
    # parent node val can be updated as the max(left.val, right.val) + node.val
    # keep updating max_path when visiting parent node 
    # by max(max_path, left.val + right.val + node.val)
    
    # edge cases:
    # negative node value -> the max_path initialized as the integer min value
    def __init__(self):
        self.max_path = -float('inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 
            left_val, right_val = 0,0
            if node.left is not None:
                dfs(node.left)
                left_val = node.left.val
            if node.right is not None:
                dfs(node.right)
                right_val = node.right.val
            # at a node, all possible path involving a node are: left child + node, 
            # right child + node, left child + node + right child, the node itself
            self.max_path = max(self.max_path, left_val + node.val, left_val + right_val + node.val, right_val + node.val, node.val)
            node.val = max(left_val, right_val, 0) + node.val
        
        dfs(root)
        return self.max_path
