def get_word_count(book_content):
    return len(book_content.split())

def get_character_count(book_content):
    book_content_cleaned = book_content.lower()
    character_dictionary = dict()
    
    for character in book_content_cleaned:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def sort_on(dictionary):
    return dictionary["num"]

def get_lst_dictionaries(character_dictionary):
    lst_dictionaries = list()
    
    for key, value in character_dictionary.items():
        lst_dictionaries.append({"char": key, "num":value})
    lst_dictionaries.sort(key=sort_on, reverse=True)

    return lst_dictionaries
    
    