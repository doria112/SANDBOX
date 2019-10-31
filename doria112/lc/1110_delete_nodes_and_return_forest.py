# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # when deleting a node, both the children could potentially become new roots
    # as long as the child is not in the list to delete
    # deletion from current tree requires to know the parent node, 
    # and if the current node is its parent's left or right node 
    # recrusively traverse the tree, and update the new roots list,
    # at each node and with its children's returned new roots
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def traverse(root:TreeNode, to_delete: List[int], parent:TreeNode, is_left) -> List[TreeNode]:
            if (root.val in to_delete) & (parent is not None):
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            new_roots = []
            if root.left:
                if (root.val in to_delete) & (root.left.val not in to_delete):
                    new_roots.append(root.left)
                new_roots.extend(traverse(root.left, to_delete, root, True))
            if root.right:
                if (root.val in to_delete) & (root.right.val not in to_delete):
                    new_roots.append(root.right)
                new_roots.extend(traverse(root.right, to_delete, root, False))
            return new_roots

        if not root:
            return []
        else: 
            if root.val not in to_delete:
                return [root] + traverse(root, to_delete, root, True)
            else: 
                return traverse(root, to_delete, None, True)
