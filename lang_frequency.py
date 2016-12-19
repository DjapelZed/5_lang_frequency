from collections import Counter


def load_data(filepath):
    file_open = open(filepath,'r')
    file_data = file_open.read()
    data = file_data.split()
    return data


def get_most_frequent_words(text):
#TODO: Игнорировать символ "—".
    cntr = Counter(text)
    return cntr.most_common(10)


if __name__ == '__main__':
    print(get_most_frequent_words(load_data(input('File path: '))))