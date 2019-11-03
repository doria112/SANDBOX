class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
# time complexity O(n), n is the number of nodes
# space complexity O(1)
