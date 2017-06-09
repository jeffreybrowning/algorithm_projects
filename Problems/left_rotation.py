# https://www.hackerrank.com/challenges/ctci-array-left-rotation
from collections import deque


def deque_left_rotation(iterable, k):
    d = deque(iterable)
    d.rotate(-k)
    return d


def array_left_rotation(iterable, k):
    # if k is larger than n
    n = len(iterable)
    if k > n:  # find the modulus of k and n to reduce amount of logic
        k = k % n

    # if k = n
    if k == n or k == 0:
        return iterable

    # k is between 1 and n, exclusive
    return iterable[k:] + iterable[:k]

if __name__ == '__main__':
    l1 = [1,2,3,4,5]
    l2 = [1,2,3,4,5]
    l3 = [1,2,3,4,5]
    print('deque-based rotation of indexes')
    print('{} rotated by {} => {}'.format(l1, 4, deque_left_rotation(l1, 4)))
    print('{} rotated by {} => {}'.format(l1, 8, deque_left_rotation(l1, 8)))
    print('{} rotated by {} => {}'.format(l1, 0, deque_left_rotation(l1, 0)))

    print('\narray-based rotation of indexes')
    print('{} rotated by {} => {}'.format(l1, 4, array_left_rotation(l1, 4)))
    print('{} rotated by {} => {}'.format(l1, 8, array_left_rotation(l1, 8)))
    print('{} rotated by {} => {}'.format(l1, 0, array_left_rotation(l1, 0)))