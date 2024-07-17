#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([(root, 0)])
        ans = []
        prev_level = None
        while queue:
            node, level = queue.popleft()
            if prev_level != level:
                ans.append(node.val)
                prev_level = level
            else:
                ans[level] = node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return ans
# @lc code=end
