def get_strings_len_bigger_ten(strings):
    long_strings = []
    for string in strings:
        if len(string) > 10:
            long_strings.append(string)
    print(long_strings)


list_my = ['black', 'whiteeeeeeeeeee', 'blueeeeeeeeeeeeee', 'orange', 'green']
get_strings_len_bigger_ten(list_my)

list_my2 = ['black', 'white', 'blue', 'orangeeeeeeeeeeeeee', 'greennnnnnnnnnnnnnnnn']
get_strings_len_bigger_ten(list_my2)

list_my3 = ['blackkkkkkkkkkk', 'white', 'blue', 'orangeeeeeeeeeeeee', 'green']
get_strings_len_bigger_ten(list_my3)
