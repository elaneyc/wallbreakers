# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def depth(p):
            if not p:
                return 0
            left, right = depth(p.left), depth(p.right)
            left = left + 1 if p.left and p.left.val == p.val else 0
            right = right + 1 if p.right and p.right.val == p.val else 0
            self.longest = max(self.longest, left + right)
            return max(left, right)

        depth(root)
        return self.longest
