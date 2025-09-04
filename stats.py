def get_word_count(content):
    list = content.split()
    return len(list)

def get_char_count(content):
    charcount = {}
    content = content.lower()

    for char in content:
        if char not in charcount:
            charcount[char] = 1
        elif char in charcount:
            charcount[char] += 1

    return charcount

def sort_list(dictionary):
    list = dictionary_to_list(dictionary)
    list.sort(reverse=True, key=sort_on)
    return list

def dictionary_to_list(dictionary):
    list = []
    for char in dictionary:
        list.append({"char": char, "num": dictionary[char] })
    return list

def sort_on(items):
    return items["num"]

