def insertionsort(l):
    """insertionsort is a sorting algrorithm similar to selection sort, 
    although with a much better best case time complexity: quadratic vs. 
    linear. 

    Insertion sort is very simple:

        1.  i increments to the length of our list
        2.  j decrements from i to beginning of the list
        3.  key is compared to list[j]. When key is larger or j underflows,
            replace l[j + 1] with our key. 

    Insertionsort has the following time and space complexities:

        Best Case Time Complexity:      O(n)
        Avg Case Time Complexity:       O(n^2)
        Worst Case Time Complexity:     O(n^2)
        Worst Case Space Complexity:    O(1)

    Pros:
        - Very simple
        - Efficient for small data sets over Quicksort, Heapsort and Mergesort.
        - Adaptive
            for pre-sorted/near-sorted the time complexity is already O(n + d),
            where d is the number of inversions. 
        - Better than other n^2 sorts (bubble/selection)
        - Stable
        - In-place
        - Online (can sort a list as it receives it)

    Cons:
        - Slower than Quicksort, Heapsort and Mergesort for large collections.
    """

    for i in xrange(len(l)):
        j = i - 1                         # j begins as element left of our i 
        key = l[i]
        while (l[j] > key) and (j >= 0):  # if the left element is bigger than the right
            l[j + 1] = l[j]               # move left element to the right
            j -= 1                        # decrement j, continue to find right place for key
        l[j + 1] = key                    # key is larger than l[j], place it into list to left of l[j] 
    return l 

