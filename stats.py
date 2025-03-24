def words_counter(string) -> int:
    contents = string.replace('\n', ' ')
    return len([i for i in contents.split(' ') if i])


def char_counter(string) -> dict:
    char_counts = {}
    for i in string.lower():
        char_counts[i] = char_counts.get(i, 0) + 1
    return char_counts


if __name__ == '__main__':
    words_counter()
