#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder_traversal(root):
            current_node = root
            stack = []
            nums = []
            while current_node or stack:
                while current_node:
                    stack.append(current_node)
                    current_node = current_node.left
                current_node = stack.pop()
                nums.append(current_node.val)
                current_node = current_node.right
            return nums
        nums = inorder_traversal(root)
        lower, upper = -2**31, 2**31-1
        stack = [(root, root.val, lower, upper)]
        wrong_answers = []
        while stack and len(wrong_answers) < 2:
            node, val, lower, upper = stack.pop()
            if node.right:
                if node.right.val > val and node.right.val < upper:
                    stack.append((node.right, node.right.val, val, upper))
                else:
                    wrong_answers.append(node.right)
            if node.left:
                if node.left.val < val and node.left.val > lower:
                    stack.append((node.left, node.left.val, lower, val))
                else:
                    wrong_answers.append(node.left)

# @lc code=end
