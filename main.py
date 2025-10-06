from stats import get_character_count

def get_book_test(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_test(filepath)
    character_dictionary = get_character_count(book_content)
    print(character_dictionary)

main()