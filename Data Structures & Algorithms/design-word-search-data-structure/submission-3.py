class Trie:
    def __init__(self,end = False):
        self.children = {}
        self.end_of_word = end

class WordDictionary:

    def __init__(self):
        self.tr = Trie(False)

    def addWord(self, word: str) -> None:
        temp = self.tr
        for letter in word:
            if not letter in temp.children:
                temp.children[letter] = Trie(False)
            temp = temp.children[letter]
        temp.end_of_word = True

    def search(self, word: str) -> bool:
        return self.TrieSearch(self.tr,word,0)

    def TrieSearch(self,trie,word,i)->bool:
        if i == len(word):
            return trie.end_of_word
        elif word[i] in trie.children:
            return self.TrieSearch(trie.children[word[i]],word,i+1)
        elif word[i] == ".":
            for key in trie.children:
                if self.TrieSearch(trie.children[key],word,i+1):
                    return True
        return False