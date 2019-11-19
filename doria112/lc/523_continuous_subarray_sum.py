class Solution:
    # approach 1 - brutal force
    # use two nested loops to represent start and end of the subarray
    # approach 2 - use mod, by making use of the info 'times of k'
    # calculate accumulative sum, thebn remainder of mod 6,
    # if we ever run into the same remainder, it means the subarray from last time we had this remainder till the current number is a times of k
    # edge case: k = 0
    # edge case: exact division at the beginning of the array, [6,6] 6
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i,j in zip(nums, nums[1:]):
                if i ==0 and j== 0:
                    return True
            return False
        remainder = {}
        remainder[0] = -1
        partial_sum = 0
        for i, n in enumerate(nums):
            partial_sum += n
            rem = partial_sum % k if k != 0 else 0
            if rem in remainder:
                if i-remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i
        return False
        
