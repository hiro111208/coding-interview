#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        prev_level = None
        sums = []
        while queue:
            node, level = queue.popleft()
            if level != prev_level:
                sums.append(node.val)
                prev_level = level
            else:
                sums[level] += node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return sums.index(max(sums)) + 1
# @lc code=end
