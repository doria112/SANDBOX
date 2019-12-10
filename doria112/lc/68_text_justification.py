class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # edge case: one word in a line, all spaces are to the right
        # no space to the right unless the last line, or only one word in a line
        res = []
        n = 0
        count = 0
        cur = []
        while n < len(words):
            if count + len(words[n]) <= maxWidth:
                cur.append(words[n])
                count += (len(words[n]) +1)
                n += 1
            else:
                count -= 1
                m = len(cur)
                space = maxWidth - count
                if m <= 1:
                    line = cur[0] + ' '* space
                else:
                    residual = space % (m-1)
                    even = (space - residual)/(m-1)
                    line = ''
                    for i,c in enumerate(cur[:-1]):
                        line += (c + ' '*(int(even)+1))
                        if i < residual:
                            line += ' '
                    line += cur[-1]
                res.append(line)
                count = 0
                cur = []

        # there is always at least one word in cur
        line = ' '.join(cur)
        line += ' '*(maxWidth - len(line))
        res.append(line)

        return res
