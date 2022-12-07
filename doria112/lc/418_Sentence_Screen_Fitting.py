# brutal force exceeding time limit
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ans = 0
        index = 0
        for i in range(rows):
            space = cols

            while space >= len(sentence[index]):
                space -= len(sentence[index])
                index += 1
                if index == len(sentence):
                    index = 0
                    ans += 1
                if space > 0:
                    space -= 1
        return ans
