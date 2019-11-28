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


# Optimized, by treating ( and ) symetrically and scanning twice - left to right, and right to left
class Solution:
    # can't break down input string by pieces, 
    # a later invalid parenthesis can still be fixed by an already fixed part 
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def fix(s, start, end, op, cp): # open_parenthesis, closed_parenthesis
            valid_set = set()
            if start >= end:
                return valid_set
            # need to fix from start to i
            for j in range(end-1, start-1, -1):
                if s[j] == cp and (j == start or s[j-1] != cp):
                    valid_set.add(s[start:j]+s[j+1:])
            return valid_set
        
        # after fixing a part, resemble the original string
        def checkOneDirection(to_fix, op, cp):
            valid_prefix = to_fix
            while True:
                new_valid_prefix = set()
                for s in valid_prefix:
                    stack = 0
                    # TODO this loop may not need to start from 0
                    for i in range(len(s)):
                        if s[i] == op:
                            stack += 1
                        elif s[i] == cp:
                            stack -= 1
                        if stack < 0:
                            # TODO can update the start of this for loop to i (not i+1, since we have removed one from 0/start to i)
                            new_fixed_set = fix(s, 0, i+1, op, cp)
                            for fixed in new_fixed_set:
                                new_valid_prefix.add(fixed)
                            break
                if len(new_valid_prefix) == 0:
                    break
                valid_prefix = new_valid_prefix
            return valid_prefix
        
        valid_left_to_right = checkOneDirection(set([s]), '(', ')')
        rl_set = set()
        for lr in valid_left_to_right:
            t = ''.join(reversed(lr))
            rl_set.add(t)
        valid_right_to_left = checkOneDirection(rl_set, ')', '(')
        
        valid = set()
        for rl in valid_right_to_left:
            valid.add(''.join(reversed(rl)))
        return valid
