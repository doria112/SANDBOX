class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        si, ei = [], []
        def reduce_string(original):
            return [[c, i] for i, c in enumerate(original) if c == "L" or c == "R"]
        si = reduce_string(start)
        ei = reduce_string(end)

        if len(si) != len(ei):
            return False
        for i in range(len(si)):
            if si[i][0] != ei[i][0] or (si[i][0] == "L" and si[i][1] < ei[i][1]) or (si[i][0] == "R" and si[i][1] > ei[i][1]):
                return False
        return True
