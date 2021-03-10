# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, m: int) -> int:
            if not node:
                return 0
            if node.val >= m:
                res = 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            else:
                res = dfs(node.left, m) + dfs(node.right, m)
            return res
        
        return dfs(root, float('-inf'))
