#!/usr/bin/env python3

import random
import textwrap

from Exercise03 import build_successor_map


def generate_text(successor_map, word_count=50):
    """Generate a requested number of words from a bigram successor map."""
    if not successor_map:
        return []

    bigram = random.choice(list(successor_map))
    generated_words = []

    for _ in range(word_count):
        next_words = successor_map.get(bigram)

        # A bigram at the very end of the source text may have no successor.
        # If that happens, choose a fresh starting point.
        if not next_words:
            bigram = random.choice(list(successor_map))
            next_words = successor_map[bigram]

        word = random.choice(next_words)
        generated_words.append(word)
        bigram = (bigram[1], word)

    return generated_words


def main():
    file_path = 'files/dr_jekyll_and_mr_hyde.txt'
    successor_map = build_successor_map(file_path)

    generated_words = generate_text(successor_map, 50)
    generated_text = ' '.join(generated_words)

    print(textwrap.fill(generated_text, width=75))


if __name__ == '__main__':
    main()
