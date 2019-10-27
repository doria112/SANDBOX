class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # n - number of password digits
        # k - number of available digit values
        num_vertices = k**n
        def permute(in_pwd, k, seen):
            if len(seen) == num_vertices:
                print(seen)
                return True
            for v in range(k):
                candidate = in_pwd[1:] + str(v)
                if candidate in seen:
                    continue
                else:
                    seen.append(candidate)
                    found = permute(candidate, k, seen)
                    if not found:
                        seen.pop() # remove candidate
                    else:
                        return True
            return False
        seen = []
        # start from all 0s
        start = '0'*n
        seen.append(start)
        found = permute(start, k, seen)

        for s in seen[1:]:
            start += s[-1]
        return start
        
solution = Solution()
# 0,0 0,2 1,2
print(solution.crackSafe(3,2))
