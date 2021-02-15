# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        nodeList = []
        def dfs(currentNode: TreeNode, nodeList: list):
            if currentNode:
                nodeList.append(str(currentNode.val))
                dfs(currentNode.left, nodeList)
                dfs(currentNode.right, nodeList)
            else:
                nodeList.append('N') 
            return
        dfs(root, nodeList)
        return ','.join(nodeList)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def dfs(nodeList: list, idx: int):
            val = nodeList[idx]
            if val == 'N':
                node = None
            else:
                node = TreeNode(int(val))
                node.left, idx = dfs(nodeList, idx+1)
                node.right, idx = dfs(nodeList, idx+1)
            return node, idx
        
        nodeList = data.split(',')
        root, _ = dfs(nodeList, 0)
        return root
