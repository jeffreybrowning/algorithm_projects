def sieve(n):
    """Efficient algorithm for determining the prime numbers up
    to upper bound n. The Seive of Eratosthenes is quick up to
    n of around 10,000.

    The Seive of Eratosthenes has the following space and time
    complexities:

        Time:  O(nloglogn) Based on the summation of the harmonic series
        Space: O(n)

    The algorithm has the following steps:

        1.  Create a list of consecutive counting numbers up
            to n from 2.
        2.  Starting with 2, for every element which has not been
            elminated, store that value as prime and remove all of
            its multiples from the list. If n is 10, we would start
            at 2, store it as prime, then remove 4, 6, 8 and 10.
        3.  Continue through the list placing any non-eleminated
            number into a list of primes, and removing its multiples.
        4.  When the ith element of the iteration squared is larger than
            the upper bound n, no further work is required. All values
            above this must be prime.
    """

    number_list = range(2, n)
    primes = []

    for i in number_list:
        if i*i >= n:
            return primes + [x for x in number_list[i:] if x]

        if i:
            primes.append(i)
            for j in range(i*i, n, i):
                number_list[j - 2] = False
