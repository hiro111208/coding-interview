#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # https://www.youtube.com/watch?v=qB0zZpBJlh8
        stack = []
        for char in s:
            if char == "]":
                chars = ""
                while stack[-1] != "[":
                    chars = stack.pop() + chars
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * chars)
            else:
                stack.append(char)
        return "".join(stack)


# @lc code=end
