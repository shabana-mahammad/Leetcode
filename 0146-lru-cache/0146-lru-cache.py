from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.mp=OrderedDict()

    def get(self, key: int) -> int:
        if key in self.mp:
            self.mp.move_to_end(key)
            return self.mp[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp.move_to_end(key)
        self.mp[key]=value  
        if len(self.mp)>self.cap:
            self.mp.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)