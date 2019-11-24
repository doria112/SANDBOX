class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        sorted(nums1), sorted(nums2)
        
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            # increment the index of the smaller number
            elif nums1[i] < nums2[j]: 
                i += 1
            else:
                j += 1
        return intersection
