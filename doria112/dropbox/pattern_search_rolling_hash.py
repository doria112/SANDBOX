class Hash: # CamelCase
    def __init__(self, prime):
        self.prime = prime
        self.current_pos = 0
        self.current_hash = 0
        
    def __str__(self):
        return f"{self.prime}"
    
    def rolling_hash(self, pos, text, pl): # pl - pattern length
        if pos+pl > len(text):
            raise Exception("overflow")
        incr = 0
        # update hash
        for i in range(self.current_pos, pos):
            self.current_hash -= self.prime ** (pl-1-i+self.current_pos) * (ord(text[i])-ord('a'))
            incr = incr * self.prime + (ord(text[i+pl]) - ord('a'))
        self.current_hash *= self.prime ** (pos - self.current_pos)
        self.current_hash += incr
        self.current_pos = pos
        print(f"current pos {self.current_pos} current hash {self.current_hash}")
        return self.current_hash
    
    def get_hash(self, t):
        hash = 0
        for i in range(0, len(t)):
            hash = hash * self.prime + ord(t[i]) - ord('a')
        return hash

class SearchPattern:
    def __init__(self, pattern, text, prime):
        self.pattern = pattern
        self.text = text
        
    def exact_search(self, pattern, text): 
        l = len(pattern)
        return l == len(text) and all(pattern[i] == text[i] for i in range(l))
    
    def naive_search(self, pattern, text):
        # at each text pos, compare with pattern 
        # time complexity O((N-L)*L) ~ O(N^L)
        for i in range(len(text) - len(pattern) + 1):
            if self.exact_search(pattern, text[i:i+len(pattern)]):
                return f"found at {i}"
        return "not found"
    
    def search_pattern(self):
        pl = len(self.pattern)
        hash = Hash(7)
        hash.current_hash = hash.get_hash(self.text[0:pl])

        pattern_hash = hash.get_hash(self.pattern)
        print(pattern_hash)
        for i in range(0, len(self.text)-pl+1):
            print(i, hash.current_hash)
            if hash.rolling_hash(i, self.text, 2) == pattern_hash:
                # perform exact search
                if self.exact_search(self.pattern, self.text[i:i+pl]):
                    return f"found at {i} - {self.text[i:i+pl]}" 
        return -1 # not found

sp = SearchPattern("bc", "ddBcbc", 7)
print(sp.search_pattern())
print(sp.exact_search("bc", "bcc"))
print(sp.naive_search("bc", "abcc"))
