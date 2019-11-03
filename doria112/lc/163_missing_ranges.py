class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatOutput(lower, upper):
            if upper > lower:
                return str(lower)+'->'+str(upper)
            return str(lower)
            
        if not nums:
            # lower and upper inclusive
            return [formatOutput(lower, upper)]
        res = []
        if lower < nums[0]:
            # missing one or more
            res.append(formatOutput(lower, nums[0] - 1))
        for i,num in enumerate(nums):
            if i == len(nums)-1:
                # compare with upper
                if num < upper:
                    res.append(formatOutput(num+1, upper))
            else:
                # compare with next in nums
                if nums[i+1] - num > 1:
                    res.append(formatOutput(num+1, nums[i+1]-1))
        return res

solution = Solution()
print(solution.findMissingRanges([0,1,3,50,75], 0, 99)
print(solution.findMissingRanges([], 0, 99)
# edge cases: lower/upper = integer min/max, any subtract or plus 1 will overflow
