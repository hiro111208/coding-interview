#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        self.removed.add(self.smallest)
        smallest = self.smallest
        while self.smallest in self.removed:
            self.smallest += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
        self.smallest = min(num, self.smallest)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
