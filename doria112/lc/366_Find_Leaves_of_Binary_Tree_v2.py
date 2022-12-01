# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        all_leaves= []
        
        def getHeight(node: TreeNode , all_leaves: List[List[int]]):
            if not node:
                return -1
            height = max(getHeight(node.left, all_leaves), getHeight(node.right, all_leaves)) + 1 
            if height > len(all_leaves)-1:
                all_leaves.append([])
            all_leaves[height].append(node.val)
            return height
            
        getHeight(root, all_leaves)
        return all_leaves
            
