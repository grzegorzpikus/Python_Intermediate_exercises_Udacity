from Python_intermediate.Lesson2Test.parse_content import parse_content

text = open('contents')
text2 = text.read().strip().replace(',', ' ')
dict = parse_content(text2)


tree : dict = {}

words_list = []
for key in dict.keys():
    words_list.append(key)

numbers = []
for value in dict.values():
    numbers.append(value)


def check_add(char : str, dict : dict, word : str) -> dict:
    new_dict : dict = {}
    if word.index(char) == word.index(word[-1]):
        if char in dict:
            y = dict[char]
            y['$' + word] = y.get('$' + word, numbers[words_list.index(word)])
            return dict[char]
        else:
            new_dict['$' + word] = numbers[words_list.index(word)]
            dict[char] = new_dict
            return new_dict
    else:
        if char in dict:
            return dict[char]
        else:
            dict[char] = new_dict
            return new_dict

for word in words_list:
    x : dict = tree
    for i in word:
        x = check_add(i, x, word)


print(tree)








# dict = {'ban': 10, 'band': 5, 'bar': 14, 'can': 32, 'candy': 7}


"""
{'b': 
    {'a': 
        {'n': {'$ban': 10, 
             'd': {'$band': 5}}, 
         'r': {'$bar': 14}}},
 'c': 
    {'a': 
        {'n': {'$can': 32, 
             'd': 
                {'y': {'$candy': 7}}}}}}
"""







