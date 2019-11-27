# BFS
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(input_str):
            stack = 0
            for l in input_str:
                if l == '(':
                    stack+=1
                elif l == ')':
                    stack-=1
                if stack < 0:
                    return False
            return stack == 0
        
        res = set()
        level = set([s])
        while len(res) == 0 and len(level) > 0:
            new_level = set()
            for candidate in level:
                if isValid(candidate):
                    res.add(candidate)
                else:
                    for i in range(len(candidate)):
                        new_level.add(candidate[:i]+candidate[i+1:])
            level = new_level
        return list(res) if len(res) > 0 else []

solution = Solution()
print(solution.removeInvalidParentheses("()())()"))
print(solution.removeInvalidParentheses("(a)())()"))
print(solution.removeInvalidParentheses(")("))
