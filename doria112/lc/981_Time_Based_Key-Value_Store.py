class TimeMap:

    def __init__(self):
        self.time_kv_store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_kv_store:
            self.time_kv_store[key] = {}
        self.time_kv_store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_kv_store:
            return ""
        rv = ""
        max_ts = float('-inf')
        for ts, value in self.time_kv_store[key].items():
            if ts <= timestamp and ts > max_ts:
                max_ts = ts
                rv = value
        return rv


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
