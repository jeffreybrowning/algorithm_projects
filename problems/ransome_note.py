# https://www.hackerrank.com/challenges/ctci-ransom-note

from collections import Counter

def ransom_note(magazine, ransom):
    mag_counter = Counter(magazine)
    ransome_counter = Counter(ransom)
    return ransome_counter - mag_counter == Counter([])