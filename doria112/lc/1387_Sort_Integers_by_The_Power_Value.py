from collections import defaultdict
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = defaultdict()
        def find_power(num, cache):
            if num in cache:
                return cache[num]
            if num == 1:
                return 0
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3*num + 1
            return find_power(num, cache) + 1

        rv = []
        for i in range(lo, hi+1):
            rv.append([find_power(i, cache), i])
        rv.sort()
        return rv[k-1][1]
