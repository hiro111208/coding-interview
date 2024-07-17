#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ht = list()
        curr = head
        ans = 0
        index = 0
        while curr:
            ht.append(curr.val)
            index += 1
            curr = curr.next
        for i in range(int(len(ht)/2)):
            ans = max(ans, ht[i] + ht[len(ht) - 1 - i])
        return ans

# @lc code=end
