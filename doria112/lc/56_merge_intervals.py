class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals = sorted(intervals)
        left = intervals[0][0]
        right = intervals[0][1]
        for inter in intervals[1:]:
            if inter[0] <= right:
                right = max(right, inter[1])
            else:
                res.append([left, right])
                left = inter[0]
                right = inter[1]
        res.append([left, right])
        return res
