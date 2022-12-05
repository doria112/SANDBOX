from collections import defaultdict
class DetectSquares:

    def __init__(self):
        # pt with frequency
        self.pt = defaultdict(lambda:0)
        self.x = defaultdict(list)
        self.y = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        self.pt[tuple(point)] += 1
        self.x[point[0]].append(point[1])
        self.y[point[1]].append(point[0])
        

    def count(self, point: List[int]) -> int:
        rv = 0
        same_x = self.x[point[0]]
        for x in same_x:
            height = abs(x-point[1])
            if height == 0:
                continue
            rv += self.pt[tuple([point[0]+height, x])] * self.pt[tuple([point[0]+height, point[1]])]
            rv += self.pt[tuple([point[0]-height, x])] * self.pt[tuple([point[0]-height, point[1]])]
        return rv
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
