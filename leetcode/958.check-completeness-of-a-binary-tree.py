#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        blank = False
        while queue:
            node = queue.popleft()
            if node == None:
                blank = True
            else:
                if blank:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True


# @lc code=end
