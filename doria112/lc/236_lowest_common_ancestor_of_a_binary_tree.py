class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> (int, 'TreeNode'):
            if root is None:
                return 0, None
            mid, left, right = 0, 0, 0
            if (root.val == p.val) or (root.val == q.val):
                mid = 1
            left, ln = search(root.left, p, q)
            if ln is not None:
                return 1, ln
            if mid + left == 2:
                return 1, root
            right, rn = search(root.right, p, q)
            if rn is not None:
                return 1, rn
            if mid + left + right >= 2:
                return 1, root
            elif mid + left + right > 0:
                return 1, None
            else:
                return 0, None
        found, lca = search(root, p, q)
        return lca

    
#### Version 2 ####
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.node = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root: 'TreeNode') -> int:
            if self.node:
                return 0
            if not root:
                return 0
            mid, left, right = 0, 0, 0
            if (root.val == p.val) or (root.val == q.val):
                mid = 1
            left = search(root.left)
            right = search(root.right)
            if mid + left + right >= 2:
                self.node = root
                return 1
            else:
                return (mid + left + right > 0)

        found = search(root)
        return self.node
