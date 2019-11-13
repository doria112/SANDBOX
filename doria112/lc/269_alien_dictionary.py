class Solution:
    def alienOrder(self, words: List[str]) -> str:
        pre, suf = collections.defaultdict(set), collections.defaultdict(set)
        all_letters = set()
        for i in range(len(words)-1):
            all_letters.update(set(words[i]))
            w1 = words[i]
            w2 = words[i+1]
            for j in range(len(w1)):
                if w1[j] != w2[j]:
                    pre[w2[j]].add(w1[j])
                    suf[w1[j]].add(w2[j])
                    break
        if len(words)>0:
            all_letters.update(set(words[-1]))

        order = ''
        
        while all_letters:
            new_order = order
            for l in all_letters:
                # no letters come before l, l can be added to final order
                if l not in pre:
                    new_order += l
                    all_letters.remove(l)
                    for s in suf[l]:
                        pre[s].remove(l)
                        if not pre[s]:
                            del pre[s] # make sure no query on pre[s] later, otherwise, default value set() will be inserted
                    break
            if order == new_order:
                return ""
            else:
                order = new_order
        return order
