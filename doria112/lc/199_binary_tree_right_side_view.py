# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS, keep track of the right most node on each level
    def rightSideView(self, root: TreeNode) -> List[int]:
        # level
        # new_level 
        # edge case: if root is None, what's the return value?
        if root is None:
            return []
        level = collections.deque()
        level.append(root)
        right_most = []
        while True:
            new_level = collections.deque()
            while level:
                node = level.popleft()
                if len(level) == 0:
                    right_most.append(node.val)
                if node.left is not None:
                    new_level.append(node.left)
                if node.right is not None:
                    new_level.append(node.right)
            if len(new_level) == 0:
                break
            level = new_level
            
        return right_most
