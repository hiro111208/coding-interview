#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # else:
        #     counter = 1
        #     queue = [root]
        #     while queue:
        #         node = queue.pop(0)
        #         if node.left:
        #             queue.append(node.left)
        #             counter += 1
        #         if node.right:
        #             queue.append(node.right)
        #             counter += 1
        #     return counter

        # https://www.youtube.com/watch?v=CvrPf1-flAA
        left_levels = 1
        left_node = root.left
        while left_node:
            left_node = left_node.left
            left_levels += 1
        right_levels = 1
        right_node = root.right
        while right_node:
            right_node = right_node.right
            right_levels += 1
        if right_levels == left_levels:
            return 2 ** left_levels - 1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


# @lc code=end
