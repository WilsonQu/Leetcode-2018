# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, 0)
        return root
    
    def helper(self, root, Sum):
        if not root:
            return Sum
        right = self.helper(root.right, Sum)
        root.val += right
        return self.helper(root.left, root.val)