#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # odds = ListNode()
        # currOdds = odds
        # evens = ListNode()
        # currEvens = evens
        # index = 1
        # while head:
        #     if index % 2 == 0:
        #         currEvens.next = ListNode(head.val)
        #         currEvens = currEvens.next
        #     else:
        #         currOdds.next = ListNode(head.val)
        #         currOdds = currOdds.next
        #     head = head.next
        #     index += 1
        # currOdds.next = evens.next
        # return odds.next

        # https://algo.monster/liteproblems/328
        if not head:
            return None

        odds = head
        evens = evens_head = head.next
        while evens and evens.next:
            odds.next = evens.next
            odds = odds.next

            evens.next = odds.next
            evens = evens.next

        odds.next = evens_head

        return head

# @lc code=end
