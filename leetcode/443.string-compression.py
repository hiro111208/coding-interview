#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        # if len(chars) == 1:
        #     return 1

        # s = ""
        # i = 1
        # letter = 0
        # count = 1
        # while i < len(chars):
        #     if not chars[i] == chars[letter]:
        #         s += chars[letter]
        #         if count > 1:
        #             s += str(count)
        #         letter = i
        #         count = 1
        #     else:
        #         count += 1
        #     i += 1
        # s += chars[letter]
        # if count > 1:
        #     s += str(count)
        # print(s)

        # # for i in range(len(chars)-len(s)):
        # #     chars.pop()

        # for i in range(len(s)):
        #     chars[i] = s[i]

        # return len(chars)

        # https://medium.com/@hamnaqaseem/leetcode-443-string-compression-python-solution-77b28c762e34
        i = 0
        counter = 1
        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j-1]:
                counter += 1
            else:
                chars[i] = chars[j-1]
                i = i + 1
                if counter > 1:
                    for k in str(counter):
                        chars[i] = k
                        i += 1
                counter = 1
        return i

# @lc code=end
