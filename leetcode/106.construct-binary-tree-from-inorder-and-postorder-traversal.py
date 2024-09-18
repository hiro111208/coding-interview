#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # https://youtu.be/vm63HuIU7kw?si=QXSEEde9oYFc4YrZ
        inorder_index = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())

            index = inorder_index[root.val]
            root.right = helper(index + 1, r)
            root.left = helper(l, index - 1)
            return root
        return helper(0, len(inorder) - 1)
# @lc code=end
