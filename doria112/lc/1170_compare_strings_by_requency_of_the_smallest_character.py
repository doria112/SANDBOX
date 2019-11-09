class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            return word.count(min(word))
        
        w_freq = [f(w) for w in words]
        w_freq = sorted(w_freq)
        
        res = [(len(words) - bisect.bisect(w_freq, f(q))) for q in queries]
        return res
    
solution = Solution()
print(solution.numSmallerByFrequency(["cbd"], ["zaaaz"]))
print(solution.numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"]))
print(solution.numSmallerByFrequency([], ["a","aa","aaa","aaaa"]))
print(solution.numSmallerByFrequency(["bbb"], []))
