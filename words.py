#!/usr/bin/env python3
"""Retrieves and print words from url"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a url"""
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items, one per line"""
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from an url"""
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # the 0th arg is the module filename.