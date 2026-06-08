class Trie:
    def __init__(self,end= False):
        self.children = {}
        self.end = end
class PrefixTree:

    def __init__(self):
        self.ini = Trie()

    def insert(self, word: str) -> None:
        temp = self.ini
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = Trie()
            temp = temp.children[letter]
        temp.end = True



    def search(self, word: str) -> bool:
        temp = self.ini
        for letter in word:
            if letter not in temp.children:
                return False
            else:
                temp = temp.children[letter]
        return temp.end

    def startsWith(self, prefix: str) -> bool:
        temp = self.ini
        for letter in prefix:
            if letter not in temp.children:
                return False
            else:
                temp = temp.children[letter]
        return True
        