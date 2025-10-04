def get_book_test(filepath):
    with open(filepath) as file:
        return file.read()
    
def get_word_count(book_content):
    return book_content.split()

def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_test(filepath)
    num_words = get_word_count(book_content)

main()