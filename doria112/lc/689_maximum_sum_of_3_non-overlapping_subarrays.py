class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [-1]*n
        # has to remember the sums of length-K array starting from i
        sums[0] = sum(nums[0:k])
        for i in range(1, n-k+1):
            sums[i] = sums[i-1] - nums[i-1] + nums[i+k-1]
        left = [-1] * n
        right = [-1] * n
        left[k-1] = 0
        for i in range(k, n-2*k):
            left[i] = left[i-1] if sums[left[i-1]] >= sums[i-k+1] else i-k+1
        
        right[n-k] = n-k
        for i in reversed(range(2*k, n-k)):
            right[i] = right[i+1] if sums[right[i+1]] > sums[i] else i

        max_sum = 0
        indices = []
        for i in range(k, n-k):
            cur_sum = sums[i] + sums[left[i-1]] + sums[right[i+k]]
            if cur_sum > max_sum:
                max_sum = cur_sum
                indices = [left[i-1], i, right[i+k]]
        return indices
# time complexity O(n)
# space complexity O(n)
