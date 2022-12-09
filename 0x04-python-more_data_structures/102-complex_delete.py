def complex_delete(a_dictionary, value):
    new_dic = {}
    for x, y in a_dictionary.items():
        new_dic[x] = y
    for x, y in new_dic.items():
        if y == value:
            del a_dictionary[x]
    return a_dictionary
