#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # My way
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth

        # https://www.youtube.com/watch?v=hTM3phVI6YQ

        # return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

# @lc code=end
