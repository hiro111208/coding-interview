#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # https://www.youtube.com/watch?v=vRbbcKXCxOw
        # if p == None and q == None:
        #     return True
        # if p == None or q == None or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            p_stack, q_stack = [(p, p.val)], [(q, q.val)]
            while p_stack and q_stack:
                p_node, p_val = p_stack.pop()
                q_node, q_val = q_stack.pop()
                if p_val != q_val:
                    return False
                else:
                    if p_node.left == None and q_node.left == None:
                        pass
                    elif p_node.left and q_node.left:
                        p_stack.append((p_node.left, p_node.left.val))
                        q_stack.append((q_node.left, q_node.left.val))
                    else:
                        return False
                    if p_node.right == None and q_node.right == None:
                        pass
                    elif p_node.right and q_node.right:
                        p_stack.append((p_node.right, p_node.right.val))
                        q_stack.append((q_node.right, q_node.right.val))
                    else:
                        return False
            if bool(p_stack) ^ bool(q_stack):
                return False
        return True


# @lc code=end
