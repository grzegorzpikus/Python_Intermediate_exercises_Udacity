from Udacity.Training.Python_intermediate.Lesson2Test.parse_content import parse_content


text = open('contents')
text2 = text.read().strip().replace(',', ' ')

dict = parse_content(text2)

def make_tree(words):
    trie = {}
    for word, frequency in words.items():
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[f'${word}'] = frequency
    return trie

print(make_tree(dict))