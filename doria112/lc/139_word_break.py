class Solution:
    # dp approach
    # building the dp array from left to right
    # dp[i] means the subarray ending at i can be splitted 
    # can only check if s[j:i] in dict, instead of being splitted (will cause extra work), 
    # since the splitting will be checked at a different j, 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # the base value for dp needs to be True
        for i in range(1,n+1):
            dp[i] = True if any(dp[j] and s[j:i] in wordDict for j in range(i)) else False
        return dp[n]
