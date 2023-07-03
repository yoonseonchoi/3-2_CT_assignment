ENDS_HERE = '#'

class Trie:
    def __init__(self):
        self.dic = {}
    
    def insert(self, text):
        node = self.dic
        for ch in text:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[ENDS_HERE] = True
    
    def find(self, prefix):
        node = self.dic
        for ch in prefix:
            if ch not in node:
                return []
            node = node[ch]
        return self.get(node)
    
    def get(self, node):
        res = []
        for c, v in node.items():
            if c == ENDS_HERE:
                temp = ['']
            else:
                temp = [c+s for s in self.get(v)]
            res.extend(temp)
        return res

def naiveAutocomplete(words, s):
    out = []
    for word in words:
        if word.startswith(s):
            out.append(word)
    return out

def autocomplete(words, s):
    trie = Trie()
    for word in words:
        trie.insert(word)
    outputs = trie.find(s)
    return outputs if not outputs else [s + suffix for suffix in outputs]

if __name__ == '__main__':
    words = ['cat', 'dog', 'deer', 'deal']
    s = 'de'
    print(autocomplete(words, s))