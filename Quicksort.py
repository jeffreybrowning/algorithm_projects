from random import choice

def quicksort(l):
    """quicksort is a fast comparison sorting algorithm that is asymptotically
    optional: all comparison algorithms are at least Omega of nlog(n)

    Quicksort consists of four steps:
        1.  Creates a pivot point to use as a comparison for the rest of the list.
        2.  Moves all elements with lower value than the pivot into a left list.
        3.  Moves all elements with higher value than the pivot into a right list.
        4.  Recursively calls quicksort on the cacatenation of the left, pivot and right
        lists to return a sorted array. 

    Quicksort has the following time and space complexities:
        Best Case Time Complexity:      O(nlog(n))
        Avg Case Time Complexity:       O(nlog(n))
        Worst Case Time Complexity:     O(n^2) 
        Worst Case Space Complexity:    O(n)

    Pros:
        - Optimized quicksort is faster than both mergesort and heapsort, and all
            other sorting algorithms for large data sets that are not sorted or
            near sorted
        - Optimized quicksort using insertion sort for sublists of elements from 
            8-20 long is the fastest sort available.
        - Works well with cached values
        - Rare worst case (all elements or many elements having the same value)
            This can be engineered around
    Cons:
        - Not in-place
        - Not stable if Optimized
        - O(n) space complexity can be a nightmare
    """
    if len(l) <= 1:
        return l
    pivot = l[0]

    left = [x for x in l[1:] if x < pivot]
    right = [x for x in l[1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


def rquicksort(l):
    """

    """
    if len(l) <= 1:
        return l
    pivot = choice(l)

    left = [x for x in l[:pivot] + l[pivot+1:] if x < pivot]
    right = [x for x in l[:pivot] + l[pivot+1:] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)