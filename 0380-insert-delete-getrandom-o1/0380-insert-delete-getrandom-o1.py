class RandomizedSet:

    def __init__(self):
        self.v=[]
        self.mp={}

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.v.append(val)
        self.mp[val]=len(self.v)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        idx=self.mp[val]
        last_ele=self.v[-1]
        self.v[idx]=last_ele
        self.mp[last_ele]=idx
        self.v.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()