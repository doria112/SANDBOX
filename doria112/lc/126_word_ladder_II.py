class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        wordList = set(wordList)
        current_layer = collections.defaultdict(list) # value is the path till key
        current_layer[beginWord] = [[beginWord]]
        while current_layer:
            new_layer = collections.defaultdict(list)
            for word in current_layer:
                # only adding to the final result when all paths ending with that words have been consolidated into the dictionary
                if word == endWord:
                    return current_layer[word]
                    #res.extend(new_layer[candidate])
                                
                for i,l in enumerate(word):
                    #print(i,l)
                    for nl in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + nl + word[i+1:]
                        if candidate in wordList and candidate != word:
                            # deep copy thing
                            for wl in current_layer[word]:
                                new_list = [w for w in wl]
                                new_list.append(candidate)
                                new_layer[candidate].append(new_list)

            # had to change from removal of list to removing from set to be fast enough
            wordList -= set(new_layer.keys())
            current_layer = new_layer
        
        return res
