class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        for perm in itertools.permutations(nums):
            perm = list(perm)
            a = perm[0]
            b = perm[1]
            if b == 0:
                cur_results = [a+b, a-b, a*b]
            else:
                cur_results = [a+b, a-b, a*b, a/b]
            found = any(self.judgePoint24([r] + perm[2:]) for r in cur_results)
            if found:
                return True
        return False


solution = Solution()
test_case1 = [3, 3, 8, 8] # True
test_case2 = [4, 1, 8, 7] # True
print(solution.judgePoint24(test_case1))
