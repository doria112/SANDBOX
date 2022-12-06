class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ans = 0
        len_s = len(source)
        # need to check the case that cannot form target 
        s, t = 0, 0 
        found = False

        while t < len(target):
            if s == len_s:
                s = 0
                ans += 1
                if not found:
                    return -1
                found = False
            if source[s] == target[t]:
                s += 1
                t += 1
                found = True
            else:
                s += 1
        return ans + 1
