# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        gap = False
        level = collections.deque()
        level.append(root)
        while len(level) > 0:
            node = level.popleft()
            for nn in [node.left, node.right]:
                if gap:
                    if nn is not None:
                        return False
                else:
                    if nn is None:
                        gap = True
                    else:
                        level.append(nn)
        return True
