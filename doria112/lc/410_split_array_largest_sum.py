class Solution:
    # the maximum sum is teh sum of the entire array
    # since all numbers are positive, can binary search from 1 to sum of the array
    # and greedily and sequentially cut the array into parts, 
    # as long as the part sum < the number being searched
    # not valid if the resulting number of parts > m
    def splitArray(self, nums: List[int], m: int) -> int:
        max_sum = sum(nums)
        largest_sum = max_sum
        def binarySearch(nums, left, right, largest_sum, m):
            mid_sum = left + math.floor((right-left)/2)
            #print("left={}, right={}, mid={}".format(left, right, mid_sum))
            if left > right:
                return largest_sum
            # check mid_sum works or not, if works, update largest_sum
            parts = 0
            part_sum = 0
            valid = True
            for num in nums:
                if (parts > m) or (num > mid_sum):
                    valid = False
                    break
                if part_sum + num > mid_sum:
                    parts += 1
                    part_sum = num
                else:
                    part_sum += num
            # check the last bit
            if part_sum > 0:
                parts += 1
                if parts > m:
                    valid = False
            if not valid:
                # search mid_sum to max_sum
                new_sum = binarySearch(nums, mid_sum+1, right, largest_sum, m)
                if new_sum < largest_sum:
                    largest_sum = new_sum
            else:
                largest_sum = mid_sum
                new_sum = binarySearch(nums, left, mid_sum-1, largest_sum, m)
                if new_sum < largest_sum:
                    largest_sum = new_sum
            return largest_sum
        return binarySearch(nums, 0, max_sum, largest_sum, m)
    
        
solution = Solution()
test1 = [7,2,5,10,8]
test2 = [1]
test3 = []
test4 = [1,2147483647]
test5 = [2,3,1,2,4,3] # m=5 
print(solution.splitArray(test4, 0))
