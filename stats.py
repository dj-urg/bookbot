def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    num_characters = {}
    for character in text.lower():
        if character not in num_characters:
            num_characters[character] = 1
        else:
            num_characters[character] = num_characters[character] + 1    
    return num_characters

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(num_characters):
    sorted_list = []

    for char, count in num_characters.items():
        # build a small dict for this character
        item = {
            "char": char,
            "num": count,
        }
        sorted_list.append(item)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list