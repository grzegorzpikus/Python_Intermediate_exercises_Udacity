from Lesson2Test.make_tree import make_tree
from Lesson2Test.parse_content import parse_content

# numbers = input('Enter numbers: ')
numbers = 2263

text = open('contents')
text2 = text.read().strip().replace(',', ' ')
dictionary = parse_content(text2)
tree = make_tree(dictionary)
# print(tree) #it works

numbers_str = str(numbers)

char_dict_t9 = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}



def prediction(tree_ : dict, numbers_str : str):

    if len(numbers_str) == 0:
        return chosen_words(tree_)
    else:
        list1 = []
        for char in char_dict_t9[numbers_str[0]]:
            if char in tree_:
                y = tree_[char]
                if len(numbers_str) == 1:
                    list1 += prediction(y, [])
                else:
                    list1 += prediction(y, numbers_str[1:])
        return list1


def chosen_words(tree):
    queue = []
    selected_words = []
    for key, value in tree.items():
        if '$' in key:
            selected_words.append((key[1:], value))
        else:
            queue.append(value)
    while len(queue) > 0:
        node = queue.pop(0)
        for k, v in node.items():
            if '$' in k:
                selected_words.append((k[1:], v))
            else:
                queue.append(v)
    return selected_words



print(prediction(tree, numbers_str))