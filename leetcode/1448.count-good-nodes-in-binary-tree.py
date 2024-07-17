#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        max_parent = root.val
        stack = [(root, -(10**4))]
        while stack:
            node, max_parent = stack.pop()
            if node.val >= max_parent:
                good += 1
                max_parent = node.val
            if node.right:
                stack.append((node.right, max_parent))
            if node.left:
                stack.append((node.left, max_parent))
        return good

# @lc code=end
