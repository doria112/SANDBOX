class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.times = None

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, sentence, times):
        current = self.root
        for l in sentence:
            current = current.children[l]
        if current.times is not None:
            current.times -= times
        else:
            current.times = -times
    
    def search(self, sentence, start=None):
        if start is None:
            start = self.root
        
        for l in sentence:
            start = start.children[l]
            if start is None:
                return None
        return start
    
    def findAll(self, prefix, start, res):
        if start is None:
            return res
        if start.times is not None:
            res.append((start.times, prefix))
        for k,v in start.children.items():
            res = self.findAll(prefix+k, v, res)
        return res

            
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for i,s in enumerate(sentences):
            self.trie.insert(s, times[i])
        self.current = self.trie.root
        self.prefix = ''
        
    def update(self, times):
        if self.current.times:
            self.current.times -= 1
        else:
            self.current.times = -1

    def input(self, c: str) -> List[str]:
        
        # update the times if end of sentence
        if c == '#':
            self.update(1)
            #self.trie.insert(self.prefix, 1)
            self.current = self.trie.root
            self.prefix = ''
            return []
        self.prefix += c
        self.current = self.trie.search(c, self.current)
        
        res_tuples = []
        res_tuples = self.trie.findAll(self.prefix, self.current, res_tuples)
        return [x[1] for x in sorted(res_tuples)[:3]]
