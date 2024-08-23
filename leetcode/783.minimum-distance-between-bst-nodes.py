#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # https://www.youtube.com/watch?v=joxx4hTYwcw&t=306s
        # inorder traversal
        prev, res = None, float("inf")

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node

            dfs(node.right)
        dfs(root)
        return res
# @lc code=end

