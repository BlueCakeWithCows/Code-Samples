"""Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix."""

"""Canonical solution to this task is a Trie / Radix Tree """ 
class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        
    def getChild(self, char):
        if char in self.children:
            return self.children[char]
        return None
    def addChild(self, word):
        if len(word) == 0: 
            self.end = True
            return
        
        char, rest = word[0], word[1:]
        
        if not char in self.children:
            self.children[char] = Node()
        self.children[char].addChild(rest)
    
    def getAllWords(self, word):
        words = []
        if self.end: words.append(word)
        
        for key in self.children:
            words.extend(self.children[key].getAllWords(word + str(key)))
        
        return words
    
    def getAllByPrefix(self, prefix, word = ""):
        if len(prefix) == 0: return self.getAllWords(word)
        char = prefix[0]
        
        child = self.getChild(char)
        if child:
            return child.getAllByPrefix(prefix[1:], word + char)
        return None
        
            
def build_trie(words):
    trie = Node()
    for word in words:
        trie.addChild(word)
    return trie

if __name__ == "__main__":
    dict = ["dog", "deer", "deal"]
    
    trie = build_trie(dict)
    print(trie.getAllByPrefix("de"))