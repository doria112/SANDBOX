class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1,len(w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))
