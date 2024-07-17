#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # https://www.youtube.com/watch?v=Mao9uzxwvmc
        def dfs(left, right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return False
            else:
                return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        return dfs(root.left, root.right)

        # if root.left == None and root.right == None:
        #     return True
        # elif root.left.val != root.right.val:
        #     return False
        # else:
        #     return self.isSymmetric(root.left) and self.isSymmetric(root.right)


# @lc code=end
