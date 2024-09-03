#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class Node:
    def __init__(self, key=-1, value=-1, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    # https://youtu.be/cNWsgbKwwoU?si=tQr1dimJWj19bCcE
    # def __init__(self):
    #     self.map = [-1] * (10 ** 6 + 1)

    # def put(self, key: int, value: int) -> None:
    #     self.map[key] = value

    # def get(self, key: int) -> int:
    #     return self.map[key]

    # def remove(self, key: int) -> None:
    #     self.map[key] = -1
    def __init__(self) -> None:
        self.map = [Node() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key, value):
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = Node(key, value)

    def get(self, key):
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key):
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
