# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tree1 = self.getTree(q)
        tree2 = self.getTree(p)

        return tree1 == tree2

    def getTree(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        result = []
        if root.left:
            result += self.getTree(root.left)
        else:
            result.append("null")

        if root.right:
            result += self.getTree(root.right)
        else:
            result.append("null")

        result.append(root.val)
        return result
