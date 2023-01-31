class Solution:

    def __init__(self, w: List[int]):
        self.acc_weight = []
        self.total_weight = 0
        for weight in w:
            self.total_weight += weight
            self.acc_weight.append(self.total_weight)

    def pickIndex(self) -> int:
        target = self.total_weight * random.random()
        low, high = 0, len(self.acc_weight)
        while low < high:
            mid = low + (high - low)//2
            if self.acc_weight[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
