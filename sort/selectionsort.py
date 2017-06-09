def selectionsort(l):
    """selection sort is a slow sort, it is a simplistic implementation
    of insertion sort and heapsort.

    Selection sort is very simple:

        1.  i increments the indexes of our list
        2.  minimum holds the smallest value in the list
        3.  For every i, trade the current minimum in the unsorted list. 

    Selection sort has the following time and space complexities:

        Best Case Time Complexity:      O(n^2)
        Avg Case Time Complexity:       O(n^2)
        Worst Case Time Complexity:     O(n^2)
        Worst Case Space Complexity:    O(1)

    Pros:
        - no other sorting algorithm has less space movement. Only two 
        elements are switched in every loop of our range. 
        - In-place, O(1) space Complexity
        - Used when writing is slow but reading is fast
            This is the case for flash memory
    Cons:
        - Best-case time complexity is quadratic.
        - Worse than insertion sort. Often not a good reason to use This
        instead of insertion sort. 
    """

    for i in range(0, len(l) - 1):
        minimum = min(range(i, len(l)), key = l.__getitem__) 
        l[i], l[minimum] = l[minimum], l[i]
    return l
