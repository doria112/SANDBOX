# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        all_leaves = []
        
        def traverse(root: TreeNode, current_leaves):
            if not root.left and not root.right:
                current_leaves.append(root.val)
                return True
            if root.left:
                if traverse(root.left, current_leaves):
                        root.left = None
            if root.right:
                if traverse(root.right, current_leaves):
                        root.right = None
            return False

            
        while root:
            current_leaves = []
            if traverse(root, current_leaves):
                all_leaves.append(list(current_leaves))
                break
            all_leaves.append(list(current_leaves))
        return all_leaves

    
# assume the height of the tree is h, number of nodes is N
# this version of solution requires traverse the tree for h times
# each traverse will take O(N), total time complexity is h*O(N), worst case scenario is a tree with only left children, N will be decrease by 1 in each traverse. 1+2+...+N = O(N^2)
