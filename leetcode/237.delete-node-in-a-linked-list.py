#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # curr = node
        # next_node = node.next
        # while next_node:
        #     curr.val, curr.next = next_node.val, next_node.next
        #     next_node = curr.next
        #     curr = next_node

        # https://www.youtube.com/watch?v=urzP1YbgUnU
        node.val = node.next.val
        node.next = node.next.next

# @lc code=end
