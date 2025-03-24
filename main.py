def get_book_text(dir) -> str:
    with open(dir, 'r') as f:
        return f.read()


def words_counter(string) -> int:
    contents = string.replace('\n', ' ')
    return len([i for i in contents.split(' ') if i])


def main():
    book = 'books/frankenstein.txt'
    contents = get_book_text(book)
    word_counts = words_counter(contents)

    print(f'{word_counts} words found in the document')


if __name__ == '__main__':
    main()
