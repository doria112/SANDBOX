class TimeMap:
    # hash map with list of (timestamp, value) pairs
    # get: perform binary search on the first element of the list of pairs
    # set: same as get, also insert on the found index
    # need to take care of finding index 0 v.s. 1

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = {}
    
    def binarySearch(self, arr, start, end, timestamp):
        if start == end:
            if arr[0][0] <= timestamp:
                return start
            else:
                return -1
        mid = math.floor((start + end) / 2)
        if arr[mid+1][0] > timestamp:
            return self.binarySearch(arr, start, mid, timestamp)
        else:
            return self.binarySearch(arr, mid+1, end, timestamp)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[timestamp, value]]
        else:
            values = self.store[key]
            pos = self.binarySearch(values, 0, len(values)-1, timestamp)
            values.insert(pos+1, [timestamp, value])
            self.store[key] = values

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        values = self.store[key]
        pos = self.binarySearch(values, 0, len(values)-1, timestamp)
        if pos == -1:
            return ''
        return values[pos][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
