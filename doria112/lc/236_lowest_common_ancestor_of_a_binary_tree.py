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
