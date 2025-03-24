from stats import *


def get_book_text(dir) -> str:
    with open(dir, 'r') as f:
        return f.read()


def main():
    book = 'books/frankenstein.txt'
    contents = get_book_text(book)
    word_counts = words_counter(contents)
    char_counts = char_counter(contents)

    print(f'{word_counts} words found in the document')
    print(char_counts)


if __name__ == '__main__':
    main()
