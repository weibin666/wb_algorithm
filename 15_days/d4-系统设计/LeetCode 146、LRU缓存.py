'''
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4

提示：
- 1 <= capacity <= 3000
- 0 <= key <= 10000
- 0 <= value <= 105
- 最多调用 2 * 10^5 次 get 和 put
'''
class ALNode:
    def __init__(self, val):
        self.val = val
        self.nextNode = None
        self.preNode = None

class LRUCache:
    def __init__(self, capacity: int):
        self.maps = {}
        self.head = ALNode(-1)
        self.tail = ALNode(-1)
        self.capacity = capacity
        self.length = 0
        self.head.nextNode = self.tail
        self.tail.preNode = self.head

    def get(self, key: int) -> int:
        if key in self.maps:
            cur = self.maps[key][0]
            preNode = cur.preNode
            nextNode = cur.nextNode
            preNode.nextNode = nextNode
            nextNode.preNode = preNode
            tmp = self.head.nextNode
            self.head.nextNode = cur
            cur.nextNode = tmp
            tmp.preNode = cur
            cur.preNode = self.head
            return self.maps[key][1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            cur = self.maps[key][0]
            preNode = cur.preNode
            nextNode = cur.nextNode
            preNode.nextNode = nextNode
            nextNode.preNode = preNode
            tmp = self.head.nextNode
            self.head.nextNode = cur
            cur.nextNode = tmp
            tmp.preNode = cur
            cur.preNode = self.head
            self.maps[key] = [cur, value]
            return
        if self.length == self.capacity:
            delNode = self.tail.preNode
            delPreNode = self.tail.preNode.preNode
            delPreNode.nextNode = self.tail
            self.tail.preNode = delPreNode
            del self.maps[delNode.val]
            self.length -= 1
        cur = ALNode(key)
        tmp = self.head.nextNode
        self.head.nextNode = cur
        cur.nextNode = tmp
        tmp.preNode = cur
        cur.preNode = self.head
        self.maps[key] = [cur, value]
        self.length += 1
