from collections import Counter


def load_data(filepath):
    file_open = open(filepath,'r')
    file_data = file_open.read()
    data = file_data.split()
    return data


def get_most_frequent_words(text):
    cntr = Counter(text)
    top_words = cntr.most_common(10)
    return top_words


def print_most_frequent_words(top_words):
    for word_number, word in enumerate(top_words):
        print('{0}. {1}: {2}'.format(word_number + 1, word[0], word[1]))


if __name__ == '__main__':
    print_most_frequent_words(get_most_frequent_words(load_data(input('File path: '))))