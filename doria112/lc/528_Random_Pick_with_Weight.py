from sortedcontainers import SortedList
import random
class Solution:
    def __init__(self, w: List[int]):
        self.acc_w = SortedList()
        self.acc_w.add(w[0])
        for i in range(len(w)-1):
            self.acc_w.add(self.acc_w[i] + w[i+1])

    def pickIndex(self) -> int:
        l = len(self.acc_w)
        rd = random.randrange(0, self.acc_w[l-1])
        return self.acc_w.bisect_right(rd)
