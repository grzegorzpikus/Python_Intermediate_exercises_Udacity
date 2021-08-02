
text = open('contents')
text2 = text.read().strip().replace(',', ' ')

def parse_content(text2):
    dict_words = dict()
    list1 = text2.split('\n')
    list_str = []
    list_int = []

    for i in list1:
        x = i.split()
        list_str.append(x[0])
        list_int.append(x[1])

    for i in range(len(list_str)):
        dict_words[list_str[i]] = list_int[i]

    return dict_words






