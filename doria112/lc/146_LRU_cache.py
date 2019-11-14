class LRUCache:
    # clarify what 'used' mean, here both get and put
    # alternatively, can also inherent from OrderedDict by changing the signature to class LRUCache(OrderedDict)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered_dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
            return self.ordered_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key)
        self.ordered_dict[key] = value
        if len(self.ordered_dict) > self.capacity:
            self.ordered_dict.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
