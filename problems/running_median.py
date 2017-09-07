l = [12,
4,
5,
3,
8,
7]

from sort.heapsort import siftdown


if __name__ == '__main__':
    y = []
    for x in l:
        y.append(x)
        for start in range((len(y) - 2) // 2, -1, -1):
            siftdown(y, start, len(y) - 1)



        print('foo')