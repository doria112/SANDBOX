class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, l in enumerate(s):
            if counts[l] == 1:
                return i
        return -1
