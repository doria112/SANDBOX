class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = collections.Counter(s1)
        counts2 = collections.Counter()
        for i in range(len(s2)-len(s1) + 1):
            if i == 0:
                counts2 = collections.Counter(s2[:len(s1)])
            else:
                counts2[s2[i-1]] -= 1
                if counts2[s2[i-1]] == 0:
                    counts2.pop(s2[i-1])
                counts2[s2[i + len(s1) -1]] += 1
            #print(i, counts1, counts2)
            if counts1 == counts2:
                return True
        return False
