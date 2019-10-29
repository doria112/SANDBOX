class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1:
            return 3
            
        big_num = 10**9 + 7
        no_a_cnt = [0] * (n+1)
        
        no_a_cnt[0] = 1
        no_a_cnt[1] = 2
        no_a_cnt[2] = 4
        
        for i in range(3, n+1):
            no_a_cnt[i] += (no_a_cnt[i-1] + no_a_cnt[i-2] + no_a_cnt[i-3]) % big_num
        res = no_a_cnt[n]

        for i in range(n):
            res += (no_a_cnt[i]*no_a_cnt[n-1-i]) % big_num
        
        return res % big_num
        
solution = Solution()
print(solution.checkRecord(99999))
