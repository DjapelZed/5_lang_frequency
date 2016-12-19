from collections import Counter


def load_data(filepath):
    file_open = open(filepath,'r')
    file_data = file_open.read()
    data_split = file_data.split()
    return data_split


def get_most_frequent_words(text):
    counter = Counter(text)
    most_frequent_words = counter.most_common(10)
    return most_frequent_words


def print_most_frequent_words(words):
    for word_number, word in enumerate(words):
        print('{0}. {1}: {2}'.format(word_number + 1, word[0], word[1]))


if __name__ == '__main__':
    filepath = input('File path: ')
    print_most_frequent_words(get_most_frequent_words(load_data(filepath)))