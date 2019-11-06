# TODO there are many follow-ups
# https://leetcode.com/problems/shortest-way-to-form-string/discuss/330938/Accept-is-not-enough-to-get-a-hire.-Interviewee-4-follow-up
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        res = 1
        si = 0
        ti = 0
        unused = True
        while ti < len(target):
            find = source.find(target[ti], si)
            if find >= 0:
                unused = False
                ti += 1
                si = find + 1
                if si >= len(source):
                    res += 1
                    si = 0
                    unused = True
            # need to break to avoid infinite loop
            elif si == 0:
                break
            else:
                si = 0
                res += 1
        if unused:
            res -= 1
        return res if ti == len(target) else -1

solution = Solution()
print(solution.shortestWay('abc', 'abcbc'))
print(solution.shortestWay('xyz', 'xzyxz'))
print(solution.shortestWay('abc', 'acdbc'))
