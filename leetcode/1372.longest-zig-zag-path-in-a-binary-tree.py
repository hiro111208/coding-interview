#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Assume left is 1, right is 0
        max_depth = 0
        stack = [(root, 0, None)]
        while stack:
            node, current_depth, prev_direction = stack.pop()
            max_depth = max(max_depth, current_depth)
            if node.right:
                if prev_direction == 0:
                    stack.append((node.right, 1, 0))
                else:
                    stack.append((node.right, current_depth+1, 0))
            if node.left:
                if prev_direction == 1:
                    stack.append((node.left, 1, 1))
                else:
                    stack.append((node.left, current_depth+1, 1))
        return max_depth
# @lc code=end
