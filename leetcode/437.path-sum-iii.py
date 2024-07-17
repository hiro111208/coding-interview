#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        paths = 0
        stack = [(root, 0, {0: 1})]
        while stack:
            node, current_sum, history = stack.pop()
            current_sum = node.val + current_sum
            diff = current_sum - targetSum
            paths += history.get(diff, 0)
            history[current_sum] = 1 + history.get(current_sum, 0)

            if node.right:
                stack.append((node.right, current_sum, copy.copy(history)))
            if node.left:
                stack.append((node.left, current_sum, copy.copy(history)))
        return paths

# @lc code=end
