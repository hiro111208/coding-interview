#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, set())]
        ancestor_p = None
        while stack:
            node, ancestor = stack.pop()
            ancestor |= {node.val}
            if node.val == p.val:
                ancestor_p = ancestor
                print(ancestor_p)
                break
            if node.right:
                stack.append((node.right, ancestor))
            if node.left:
                stack.append((node.left, ancestor))
        stack = [(root, set())]
        ancestor_q = None
        while stack:
            node, ancestor = stack.pop()
            ancestor |= {node.val}
            if node.val == q.val:
                ancestor_q = ancestor
                print(ancestor_q)
                break
            if node.right:
                stack.append((node.right, ancestor))
            if node.left:
                stack.append((node.left, ancestor))
        return min(ancestor_p.intersection(ancestor_q))
# @lc code=end
