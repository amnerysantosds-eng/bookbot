def get_word_count(book_content):
    return book_content.split()

def get_character_count(book_content):
    book_content_cleaned = book_content.lower()
    character_dictionary = dict()
    
    for character in book_content_cleaned:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary