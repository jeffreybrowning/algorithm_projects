# https://www.hackerrank.com/challenges/ctci-making-anagrams

from collections import Counter

def number_needed(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0

    if a == b:
        return 0

    a_counter = Counter(a)
    b_counter = Counter(b)
    a_counter.subtract(b_counter)
    return sum(abs(y) for x, y in a_counter.items())

if __name__ == "__main__":
    print(number_needed('cde', 'abc'))
    print(number_needed('', 'this is ok'))
    print(number_needed('abc', 'abc'))