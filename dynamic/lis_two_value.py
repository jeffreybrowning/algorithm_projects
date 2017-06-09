def long_inc_seq(l):
    # print(l)
    largest = 0
    n = len(l)
    seq_list = [1] * n
    # i is our current item
    # j is our previ
    for i in range(1, n):
        print('\n')
        print(seq_list)
        for j in range(0, i):
            print("i: {0}, j: {1}".format(i, j))
            print("ith: {0}, jth:{1}".format(l[i], l[j]))
            if l[i] > l[j] and seq_list[i] < (seq_list[j] + 1):
                print("new maximum!: {0}".format(seq_list[j] + 1))
                seq_list[i] = seq_list[j] + 1
    return max(seq_list)

if __name__ == "__main__":
    print(long_inc_seq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
