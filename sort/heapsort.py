def heapsort(l):
    """heapsort is a fast comparison sort that is asymptotically optimal: comparison
    sorts cannot run in faster than Omega n(log(n)). It is similar to selection sort
    and insertion sort. 

    Heapsort consists of three steps:

        1.  Creates a heap out of the list by running siftdown starting with the last
            parent of our heap (len(list) - 2/2)
        2.  Once we have a max-heap, we simply remove the beginning of our array and 
            place it at the end of our array. This is the root of the max-heap, and is 
            thus the largest value in the array.
        3.  We then rerun our siftdown function, excluding our already sorted last element, 
            to maintain the max-heap property and continue to take the top of our array 
            until no items are unsorted in our array.  
    
    Heapsort has the following time and space complexities:

        Best Case Time Complexity:      O(nlog(n))
        Avg Case Time Complexity:       O(nlog(n))
        Worst Case Time Complexity:     O(nlog(n))
        Worst Case Space Complexity:    O(1)

    Pros:
        - Heapsort is the only fast comparison sort that is in-place. It thus has
        the lowest space complexity out of mergesort, quicksort and itself. 
        - Heapsort has n(log(n)) worst case time complexity, which means its worse
        case is non-significant, unlike quicksort
        - Secure. Unlike quicksort, heapsort cannot be forced into worst-case behavior
        by engineering arrays of a certain order or consistency.
    Cons:
        - Heapsort's hidden constants in the omega notation are often larger than
        quicksort's, thus it is usually slower even though both algorithms are 
        O(nlog(n))
        - Heapsort is often slower than mergsesort because mergesort has better 
        locality of reference -- it's elements are near eachother in memeory. The
        nature of a heap makes this kind of storage impossible. 
        - Heapsort is slower than even trivial parallel implementations of mergesort.
    """

    for start in range((len(l)-2)/2, -1, -1): 
        siftdown(l, start, len(l)-1)

    for end in range(len(l)-1, 0, -1):
    l[end], l[0] = l[0], l[end] # remove root and place at end of array
        siftdown(l, 0, end - 1) # siftdown without including already sorted elements
    return l


def siftdown(lst, start, end):
    """maintains the properties of a heap for sorting to take place. Heaps
    must satisfy the heap property:

        if A is a parent node of B then the key of node A is ordered with
        respect to the key of node B with the same ordering applying accross
        the heap. 

    If A is larger than B, then all parents are of higher value than their
    children. This is called a max-heap. If the reverse is true, that B is 
    of higher value than A, then all parents must have a lower value than their
    children.

    Siblings, children of the same parent, do not have any properties in relation
    to eachother. 

    The root, the top-most parent, is thus the largest value in a max-heap and 
    the smallest in a min-heap. 

    This implementation maintains a max-heap. 

    The siftdown process consists of a number of steps:

        1.  Uses start as our root
        2.  Determines the left child of the root
        3.  If the child is outside the range of our array, it does not exist
            and we break
        4.  If a right child exists for the root node, then we check to see which
            is larger. If the right child is larger, we use that. We're trying to 
            find the larger value, of course.
        5.  If the root is less than its child, we violate the max-heap property, 
            and so we switch the child and root. 
        6.  We then follow the branch down to the children of our child to continue
            to sort the heap and maintain our max-heap property using the while loop. 
    """
    root = start
    while True:
        child = root * 2 + 1
        if child > end: #checks that there is a node to check
            break
        if child + 1 <= end and lst[child] < lst[child + 1]: #sees which is smaller, our currecnt child or the other
            child += 1 # if so, lets use the larger of the two to find the max
        if lst[root] < lst[child]: # if the root is less than the child
            lst[root], lst[child] = lst[child], lst[root]  # switch them to maintain heap
            root = child  # now lets see if the child of our child needs to be swapped, run this shit again
        else:  # didnt need to be sorted, already in the right order, remove root of heap
            break