#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current_node = root
        ans = []
        stack = []
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            ans.append(current_node.val)
            current_node = current_node.right
        return ans
# @lc code=end
