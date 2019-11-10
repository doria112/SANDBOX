class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        ans = None
        while left <= right:
            mid = left + math.floor((right - left)/2)
            days, load = 1,0
            for w in weights:
                # increment when starting a new day
                if load + w > mid:
                    days += 1
                    load = 0
                load += w

            if days <= D:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
