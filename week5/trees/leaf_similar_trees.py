# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = self.getLeaves(root1)
        leaves2 = self.getLeaves(root2)

        return leaves1 == leaves2

    def getLeaves(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        result = []
        if root.left:
            result += self.getLeaves(root.left)
        if root.right:
            result += self.getLeaves(root.right)

        return result
        
