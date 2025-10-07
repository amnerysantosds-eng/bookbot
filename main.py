import stats

def get_book_test(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_test(filepath)
    word_count = stats.get_word_count(book_content)
    character_dictionary = stats.get_character_count(book_content)
    lst_dictionaries = stats.get_lst_dictionaries(character_dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for dictionary in lst_dictionaries:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")  
main()