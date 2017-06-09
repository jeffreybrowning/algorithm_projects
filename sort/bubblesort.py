def bubblesort(l):
    """bubblesort is a sort that is useful for its simplicity in 
    teaching algorithms. It is lampooned by many in 
    the computer science community. 

    Bubblesort has :

        1.  For every element in our list, check if that element has a
            greater value than the following element.
        2.  If so, then switch the elements and continue.
        3.  Numbers 1 and 2 repeat until no changes are detected for the
            entire list. 

    Bubblesort has the following time and space complexities:

        Best Case Time Complexity:      O(n)
        Avg Case Time Complexity:       O(n^2)
        Worst Case Time Complexity:     O(n^2)
        Worst Case Space Complexity:    O(1)

    Pros:
        - bubblesort is very good at determining a near-sorted or 
        already sorted list. It is therefore better than Quicksort,
        but not better than insertion sort. 
        - bubblesort is in-place, and therefore needs only constant 
        space. 
        - Useful for computer graphics, when needing to determining 
        the relative distance to objects. When these do not change much,
        the cons of bubblesort are minimized. 
    Cons:
        Oh, there are many
        - Not good for large collections
        - Not good for reversed sorted collections (this is the worst case)
        - Small numbers at the end are a problem, as numbers only move backwards
        in index once for every loop of the xrange. 
    """

    if len(l) <= 1:
        return l

    changed = True

    while changed:  # if nothing changes, its already sorted
        changed = False
        for i in xrange(len(l) - 1):  # xrange yeilds generator in case this is large list
            if l[i] > l[i + 1]:  # if this is not true for any i, then the list is sorted
                l[i + 1], l[i] = l[i], l[i + 1]
                changed = True
    return l 