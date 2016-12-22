from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as file_data:
        text_in_file = file_data.read().lower()
        words_in_file = text_in_file.split()
    return words_in_file


def get_most_frequent_words(text):
    word_counter = Counter(text)
    count_most_frequent_words = 10
    most_frequent_words = word_counter.most_common(count_most_frequent_words)
    return most_frequent_words


def print_most_frequent_words(words):
    for word_number, word in enumerate(words):
        print('{0}. {1}: {2}'.format(word_number + 1, word[0], word[1]))


if __name__ == '__main__':
    filepath = input('File path: ')
    print_most_frequent_words(get_most_frequent_words(load_data(filepath)))