class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_l = 0
        distinct_chars = collections.OrderedDict()
        
        left_most = -1
        for i,l in enumerate(s):
            distinct_chars[l] = i
            distinct_chars.move_to_end(l)
            if len(distinct_chars) > k:
                c, left_most = distinct_chars.popitem(last=False)
                length = i - left_most 
            else:
                length = i -left_most
            max_l = max(max_l, length)
        return max_l
