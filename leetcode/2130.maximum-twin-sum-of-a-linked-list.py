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
        # ht = list()
        # curr = head
        # ans = 0
        # index = 0
        # while curr:
        #     ht.append(curr.val)
        #     index += 1
        #     curr = curr.next
        # for i in range(int(len(ht)/2)):
        #     ans = max(ans, ht[i] + ht[len(ht) - 1 - i])
        # return ans

        # https://youtu.be/doj95MelfSA?si=lKkB1Pwo7MW7zu-y
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res


# @lc code=end
