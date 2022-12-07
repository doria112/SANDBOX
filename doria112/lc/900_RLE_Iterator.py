class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.buffer = 0
        self.cn = -1 #current number
        self.encoding = encoding
        self.index = -2

    def next(self, n: int) -> int:
        while n >= self.buffer or self.buffer == 0:
            n -= self.buffer
            self.buffer = 0
            if n == 0:
                return self.cn
            self.index += 2
            if self.index >= len(self.encoding):
                return -1
            else:
                self.buffer = self.encoding[self.index]
                self.cn = self.encoding[self.index+1]
        self.buffer -= n
        return self.cn


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
