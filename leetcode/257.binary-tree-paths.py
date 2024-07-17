#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # https://walkccc.me/LeetCode/problems/0257/#__tabbed_1_3
        # ans = []

        # def dfs(root: Optional[TreeNode], path: List[str]) -> None:
        #     if not root:
        #         return
        #     if not root.left and not root.right:
        #         ans.append(''.join(path) + str(root.val))
        #         return

        #     path.append(str(root.val) + '->')
        #     dfs(root.left, path)
        #     dfs(root.right, path)
        #     path.pop()

        # dfs(root, [])
        # return ans

        stack = [(root, f'{root.val}')]
        paths = []
        while stack:
            node, path = stack.pop()
            if node.right == None and node.left == None:
                paths.append(path)
            if node.left != None:
                stack.append((node.left, path + f'->{node.left.val}'))
            if node.right != None:
                stack.append((node.right, path + f'->{node.right.val}'))
        return paths
# @lc code=end
