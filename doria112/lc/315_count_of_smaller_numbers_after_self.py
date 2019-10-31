class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # clarification - is there duplicate? - yes
        # notice merge sort has this fact -
        # when taking an element from right, that element was physicially on the right of all elements in the left, and smaller than. 
        # just need to count those
        
        # tuple (value, count of smaller right, original index)
        
        num_tuples = [[v, 0, i] for i, v in enumerate(nums)]
        
        def takeOne(is_left, part, moved_right, merged):
            cur = part.pop(0)
            if is_left:
                cur[1] += moved_right
            else:
                moved_right += 1
            merged.append(cur)
            return moved_right, merged
            
        def mergeSort(tuples):
            length = len(tuples)
            if length < 2:
                return tuples
            mid = math.floor(length/2)
            left = mergeSort(tuples[0:mid])
            right = mergeSort(tuples[mid: length])
            moved_right = 0
            # merge left and right
            merged = []
            while (len(left) > 0) or (len(right) > 0):
                if len(left) > 0:
                    if len(right) > 0:
                        if right[0][0] < left[0][0]:
                            moved_right, merged = takeOne(False, right, moved_right, merged)
                        else:
                            moved_right, merged = takeOne(True, left, moved_right, merged)
                    else:
                        moved_right, merged = takeOne(True, left, moved_right, merged)
                else:
                    moved_right, merged = takeOne(False, right, moved_right, merged)
            return merged
        
        merged = mergeSort(num_tuples)
        res = [0] * len(nums)
        for m in merged:
            res[m[2]] = m[1]
            
        return res
    
solution = Solution()
test1 = [5,1,6,2]
test2 = []
print(solution.countSmaller(test1))
