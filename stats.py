def words_counter(string) -> int:
    contents = string.replace('\n', ' ')
    return len([i for i in contents.split(' ') if i])


def char_counter(string) -> dict:
    char_counts = {}
    for i in string.lower():
        char_counts[i] = char_counts.get(i, 0) + 1
    return [{'char': k, 'count': v} for k, v in char_counts.items()]


def sort_dict(char_list) -> dict:
    def sorting(d):
        return d['count']
    char_list.sort(reverse=True, key=sorting)
    return char_list


if __name__ == '__main__':
    words_counter()
