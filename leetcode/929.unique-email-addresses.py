#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ht = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            ht.add((local, domain))
        return len(ht)


# @lc code=end
