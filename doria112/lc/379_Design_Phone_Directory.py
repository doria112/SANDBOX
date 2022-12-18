import heapq
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.q = []
        self.max = maxNumbers
        self.size = 0
        for i in range(maxNumbers):
            heapq.heappush(self.q, i)
        self.occupy = set()

    def get(self) -> int:
        if self.size < self.max:
            rv = heapq.heappop(self.q)
            self.occupy.add(rv)
            self.size += 1
            return rv
        else:
            return -1

    def check(self, number: int) -> bool:
        if number in self.occupy:
            return False
        else:
            return True

    def release(self, number: int) -> None:
        if self.check(number):
            return
        self.occupy.remove(number)
        heapq.heappush(self.q, number)
        self.size -= 1
        return 


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
