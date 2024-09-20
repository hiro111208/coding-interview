#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(u):
            u = list(reversed([*u]))
            i = 0
            while i < len(u):
                if u[i] == "#":
                    counter = 1
                    u[i] = ""
                    while i < len(u) - 1 and counter > 0:
                        i += 1
                        if u[i] == "#":
                            counter += 1
                            u[i] = ""
                        else:
                            u[i] = ""
                            counter -= 1
                i += 1
            return "".join(u)
        return helper(s) == helper(t)
# @lc code=end
