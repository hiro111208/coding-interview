#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # current_node = l1
        # arr_1 = []
        # while current_node:
        #     arr_1.append(current_node.val)
        #     current_node = current_node.next

        # current_node = l2
        # arr_2 = []
        # while current_node:
        #     arr_2.append(current_node.val)
        #     current_node = current_node.next

        # diff = len(arr_1) > len(arr_2)
        # if diff > 0:
        #     arr_2 = [0] * diff + arr_2
        # else:
        #     arr_1 = [0] * abs(diff) + arr_1
        # new_list = []
        # inc = False
        # for num_1, num_2 in zip(reversed(arr_1), reversed(arr_2)):
        #     val = num_1 + num_2 + int(inc)
        #     print(val)
        #     if val >= 10:
        #         new_list.append(val-10)
        #         inc = True
        #     else:
        #         new_list.append(val)
        #         inc = False
        # if inc:
        #     new_list = [1] + new_list
        # ans = ListNode(new_list[0])
        # curr = ans
        # for num in reversed(new_list[:-1]):
        #     curr.next = ListNode(num)
        #     curr = curr.next
        # return ans

        # https://www.youtube.com/watch?v=Kt4_jp8Dcvo
        stack_1, stack_2 = [], []

        while l1:
            stack_1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = None

        while stack_1 or stack_2 or carry:
            sum_ = carry
            if stack_1:
                sum_ += stack_1.pop()
            if stack_2:
                sum_ += stack_2.pop()

            node = ListNode(sum_ % 10)

            node.next = result
            result = node

            carry = sum_ // 10  # floor i.e. 1.4 => 1, 0.4 => 0
        return result


# @lc code=end
