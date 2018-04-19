# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.helper(s,t)
        
    def isEqual(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)
    
    def helper(self, s, t):
        if not s:
            return False
        return self.isEqual(s,t) or self.helper(s.left, t) or self.helper(s.right, t)