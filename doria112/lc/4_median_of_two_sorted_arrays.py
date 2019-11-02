class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
            
        num_left = math.ceil((m+n)/2)
        def findMedian1(first, second, nums1, nums2):
            if first < 0:
                median1 = nums2[second]
            elif second < 0:
                median1 = nums1[first]
            else:
                median1 = max(nums1[first], nums2[second])
            return median1
        
        def findMedian2(first, second, nums1, nums2):
            if first + 1 >= len(nums1):
                median2 = nums2[second+1]
            elif second + 1 >= len(nums2):
                median2 = nums1[first+1]
            else:
                median2 = min(nums1[first+1], nums2[second+1])
            return median2
        
        def binarySearch(start, end, first, second):
            # mid how many from first contributes to the left portion
            mid = start + math.floor((end - start)/2)
            second_num = num_left - mid
            if mid <= 0:
                # test second
                if mid >= len(first):
                    return mid-1, second_num-1
                if second[second_num-1] <= first[mid]:
                    return mid-1, second_num-1
                else:
                    return binarySearch(mid+1, end, first, second)
            else:
                first_max = first[mid-1]
                if first_max <= second[second_num]:
                    if second_num == 0:
                        return mid-1, second_num-1
                    elif mid >= len(first):
                        return mid-1, second_num-1
                    elif first[mid] >= second[second_num-1]:
                        return mid-1, second_num-1
                    else:
                        return binarySearch(mid+1, end, first, second)
                else:
                    return binarySearch(start, mid-1, first, second)
        
        if m <= n:
            first, second = binarySearch(0, m, nums1, nums2)
            median1 = findMedian1(first, second, nums1, nums2)
            if (m+n)%2 == 0:
                # find next, take average
                median2 = findMedian2(first, second, nums1, nums2)
                return (median1 + median2)/2
            else:
                return median1
        else:
            first, second = binarySearch(0, n, nums2, nums1)
            median1 = findMedian1(first, second, nums2, nums1)
            if (m+n)%2 == 0:
                median2 = findMedian2(first, second, nums2, nums1)
                return (median1 + median2)/2
            else:
                return median1
                
solution = Solution()
#print(solution.findMedianSortedArrays([1,3], [2]))
#print(solution.findMedianSortedArrays([1,2], [3,4]))
print(solution.findMedianSortedArrays([], [2]))
