from stats import get_word_count

def get_book_test(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_test(filepath)
    num_words = get_word_count(book_content)

main()