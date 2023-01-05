class TrieNode:
    def __init__(self, is_word):
        self.value = is_word
        self.children = {} # letter:node

class PhoneNumber:
    def __init__(self, digits, dict):
        self.digits = digits
        self.d_to_l = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.dict = set(dict)
        self.length = len(digits)
        self.words = []
        self.root = TrieNode(False)
        
    def build_trie(self, root):
        #root = TrieNode(False)
        for word in self.dict:
            self.insert_to_trie(root, word)
        return root
    
    def insert_to_trie(self, root, word):
        node = root
        for i, l in enumerate(word):
            if l not in node.children:
                is_word = (i == len(word)-1)
                node.children[l] = TrieNode(is_word)
            node = node.children[l]
    
    def start_with(self, root, prefix):
        node = root
        for l in prefix:
            if l not in node.children:
                return False
            else:
                node = node.children[l]
        return True 
    
    def search(self, root, word):
        node = root
        for l in word:
            if l not in node.children:
                return False
            else:
                node = node.children[l]
        return node.value 
        
    def brutal_force_find(self, candidate, pos):
        # end of the digits
        if len(candidate) == self.length:
            if self.is_word(candidate):
                self.words.append(candidate)
        else:
            # append the next letter
            for l in self.d_to_l[int(self.digits[pos])-0]:
                self.brutal_force_find(candidate+l, pos+1)
    
    def is_word(self, word):
        return word in self.dict
    
    def find_with_trie(self, candidate, pos):
        # end of the digits
        if len(candidate) == self.length:
            if self.search(self.root, candidate):
                self.words.append(candidate)
        elif self.start_with(self.root, candidate):
            # continue to append
            for l in self.d_to_l[int(self.digits[pos])-0]:
                self.find_with_trie(candidate+l, pos+1)
        else:
            return
            
    
pn = PhoneNumber("23", ["ae", "bd", "pc"])
#pn.brutal_force_find("", 0)
#print(pn.words)

pn.build_trie(pn.root)
pn.find_with_trie("", 0)
print(pn.words)
