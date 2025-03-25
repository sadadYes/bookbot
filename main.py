from stats import *


def get_book_text(dir) -> str:
    with open(dir, 'r') as f:
        return f.read()


def main():
    book = 'books/frankenstein.txt'
    contents = get_book_text(book)
    word_counts = words_counter(contents)
    char_counts = char_counter(contents)
    sorted = sort_dict(char_counts)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book}')
    print('----------- Word Count ----------')
    print(f'Found {word_counts} total words')
    print('--------- Character Count -------')

    for i in sorted:
        print(f'{i["char"]}: {i["count"]}')

    print('============= END ===============')


if __name__ == '__main__':
    main()
