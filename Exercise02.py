#!/usr/bin/env python3

import unicodedata


def get_book_lines(filename):
    """Return the actual book text, excluding Project Gutenberg boilerplate."""
    with open(filename, 'r', encoding='utf-8-sig') as book:
        lines = book.readlines()

    start = 0
    end = len(lines)

    for index, line in enumerate(lines):
        if line.startswith('*** START OF THE PROJECT GUTENBERG EBOOK'):
            start = index + 1
        elif line.startswith('*** END OF THE PROJECT GUTENBERG EBOOK'):
            end = index
            break

    return lines[start:end]


def get_punctuation(filename):
    """Find punctuation characters that occur in the book text."""
    punctuation_marks = {}

    for line in get_book_lines(filename):
        for char in line:
            category = unicodedata.category(char)
            if category.startswith('P'):
                punctuation_marks[char] = 1

    return ''.join(punctuation_marks)


def split_line(line):
    """Treat an em dash as a separator, then split the line into words."""
    return line.replace('—', ' ').split()


def clean_word(word, punctuation):
    """Remove punctuation from the ends of a word and make it lowercase."""
    return word.strip(punctuation).lower()


def read_words(filename):
    """Return all cleaned words from the actual book text."""
    punctuation = get_punctuation(filename)
    words = []

    for line in get_book_lines(filename):
        for word in split_line(line):
            word = clean_word(word, punctuation)
            if word:
                words.append(word)

    return words


def count_trigram(trigram, trigram_counter):
    """Increase the count for one trigram."""
    key = tuple(trigram)
    trigram_counter[key] = trigram_counter.get(key, 0) + 1


def process_word_trigram(word, window, trigram_counter):
    """Maintain a three-word sliding window and count complete trigrams."""
    window.append(word)

    if len(window) == 3:
        count_trigram(window, trigram_counter)
        window.pop(0)


def count_trigrams(filename):
    """Count every trigram in a cleaned book."""
    window = []
    trigram_counter = {}

    for word in read_words(filename):
        process_word_trigram(word, window, trigram_counter)

    return trigram_counter


def find_max(counter):
    """Return the most frequent key and its frequency."""
    max_key = max(counter, key=counter.get)
    return max_key, counter[max_key]


def main():
    file_path = 'files/dr_jekyll_and_mr_hyde.txt'
    trigram_counter = count_trigrams(file_path)

    trigram, frequency = find_max(trigram_counter)

    print('Most common trigram:', ' '.join(trigram))
    print('Frequency:', frequency)


if __name__ == '__main__':
    main()
