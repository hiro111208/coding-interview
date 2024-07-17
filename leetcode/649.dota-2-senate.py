#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # https://www.youtube.com/watch?v=zZA5KskfMuQ
        R, D = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            r, d = R.popleft(), D.popleft()
            if r > d:
                D.append(r+len(senate))
            else:
                R.append(d+len(senate))
        return "Radiant" if R else "Dire"

# @lc code=end
