class Solution:
    def expand(self, S: str) -> List[str]:
        # clarify questions:
        # within each brace, are there duplicated letters? - no. list is fine 
        # is it always single letter? - yes
        
        # recursive - each recursive call takes care of one position
        # if the current position is {, search for } and split by ,
        # for each element, call the remaining after } with updated prefix
        # if current position is not {, update the prefix
        # then recursively call the remaining string

        if S == '':
            return ['']
        words = []
        
        def breakBrace(prefix, resStr):
            if not resStr:
                if len(prefix) > 0:
                    words.append(prefix)
                return
            if resStr[0] == '{':
                end = resStr.find('}')
                for element in resStr[1:end].split(','):
                    breakBrace(prefix + element, resStr[end+1:])
            else:
                breakBrace(prefix + resStr[0], resStr[1:])
        
        breakBrace('', S)
        return sorted(words)

solution = Solution()
test1 = '{a,b,c}{e,d}'
test2 = '{}'
test3 = ''
test4= '{a,b}c{d,e}f'
print(solution.expand(test3))
