#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # https://www.youtube.com/watch?v=wgFPrzTjm7s
        # sum_ = l1.val + l2.val
        # result = ListNode()
        # curr = result
        # carry = 0
        # while l1 or l2 or carry:
        #     sum_ = carry
        #     if l1:
        #         sum_ += l1.val
        #         l1 = l1.next
        #     if l2:
        #         sum_ += l2.val
        #         l2 = l2.next
        #     curr.next = ListNode(sum_ % 10)
        #     curr = curr.next
        #     carry = sum_ // 10
        # return result.next

        carry = 0
        root = ListNode()
        curr = root
        while l1 or l2 or carry:
            l1_val, l2_val = 0, 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            sum_val = l1_val + l2_val + carry
            node_val = sum_val % 10
            carry = sum_val // 10
            curr.next = ListNode(node_val)
            curr = curr.next
        return root.next
# @lc code=end
