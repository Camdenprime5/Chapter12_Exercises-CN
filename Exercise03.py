#!/usr/bin/env python3

from Exercise02 import read_words


def add_trigram(trigram, successor_map):
    """Map the first two words to the third word as a possible successor."""
    first, second, third = trigram
    key = (first, second)
    successor_map.setdefault(key, []).append(third)


def process_word_trigram(word, window, successor_map):
    """Maintain a three-word window and add each trigram to the map."""
    window.append(word)

    if len(window) == 3:
        add_trigram(window, successor_map)
        window.pop(0)


def build_successor_map(filename):
    """Build a dictionary from bigrams to lists of possible next words."""
    window = []
    successor_map = {}

    for word in read_words(filename):
        process_word_trigram(word, window, successor_map)

    return successor_map


def main():
    file_path = 'files/dr_jekyll_and_mr_hyde.txt'
    successor_map = build_successor_map(file_path)

    print('Number of bigram keys:', len(successor_map))
    print("Successors for ('said', 'the'):")
    print(successor_map.get(('said', 'the'), []))


if __name__ == '__main__':
    main()
