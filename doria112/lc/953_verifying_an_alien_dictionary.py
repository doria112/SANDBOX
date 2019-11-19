class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i, l in enumerate(order):
            order_dict[l] = i

        for w1, w2 in zip(words[:-1], words[1:]):
            m = len(w1)
            n = len(w2)
            for i in range(m):
                # compare letters at index i in w1 and w2
                if i >= n:
                    return False
                if w1[i] == w2[i]:
                    continue
                if order_dict[w1[i]] > order_dict[w2[i]]:
                    return False
                if order_dict[w1[i]] < order_dict[w2[i]]:
                    break
        return True
