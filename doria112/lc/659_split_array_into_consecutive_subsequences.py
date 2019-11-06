class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        def attach(prev, cur):
            if prev[0] > 0:
                prev[0] -= 1
                cur[1] += 1
            elif prev[1] > 0:
                prev[1] -= 1
                cur[2] += 1
            elif prev[2] > 0:
                prev[2] -= 1
                cur[2] += 1
            else:
                cur[0] += 1
            return prev, cur
        
        def check(counts):
            return counts[0] == 0 and counts[1] == 0

        m0 = None
        prev = [0]*3
        cur = [0]*3
        for m in nums:
            # TODO probably can combine m0 is None with the last case
            if m0 is None:
                prev, cur = attach(prev, cur)
            elif m - m0 <= 1:
                if m - m0 == 1:
                    if not check(prev):
                        return False
                    prev = cur
                    cur = [0] * 3
                prev, cur = attach(prev, cur)
            else:
                if not check(prev) or not check(cur):
                    return False
                prev = [0] * 3
                cur = [0] * 3
                prev, cur = attach(prev, cur)
            m0 = m
        return check(prev) and check(cur)

        
solution = Solution()
test1 = [1,2,3,3,4,5]
test2 = []
print(solution.isPossible(test2))
