class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False
            
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        current = self.root
        for w in reversed(word):
            #current[w] = Node()
            current = current.children[w]
        current.is_word = True
                
    def search(self, query):
        # return True as soon as found a word
        current = self.root
        for l in query:
            # terminate early
            if l not in current.children:
                return False
            current = current.children[l]
            if current.is_word:
                return True
        return False
        
class StreamChecker:
    # trie with reversed order of words 
    # insert
    # special search that returns True when runs into a word 
    
    # optimization: only need to search the last 2000 queries, 
    # i.e. query queue with fixed length 2000
    
    def __init__(self, words: List[str]):
        self.queue = collections.deque(maxlen=2000)
        self.trie = Trie()
        for w in words:
            self.trie.insert(w)

    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        return self.trie.search(self.queue)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
