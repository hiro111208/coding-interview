#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head.next == None:
        #     return None
        # counter = 1
        # curr = head
        # while curr.next != None:
        #     counter += 1
        #     curr = curr.next
        # middle = counter // 2
        # prev = None
        # curr = head
        # i = 0
        # while i != middle:
        #     prev = curr
        #     curr = curr.next
        #     i += 1
        # prev.next = curr.next
        # return head

        # https://medium.com/@snehaaaa/leetcode-2095-delete-the-middle-node-of-a-linked-list-59c774ec6c9b
        if head.next == None:
            return None

        slow = head
        fast = head
        prev = None

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next
        return head

# @lc code=end
