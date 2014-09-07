from heapq import merge

def mergesort(l):
    """Mergesort is a fast, comparison sorting algorithm that is asymptotically
    optimal: any comparison algorithm is at best Omega nlogn. 

    Uses a divide-and-conquer recursive paradigm to partition an input list into
    1 element sublists. This is very quick. Then merges the sublists together with the
    merge subroutine. 

    Mergesort has the following time and space complexities:

        Best Case Time Complexity:      O(nlog(n))
        Avg Case Time Complexity:       O(nlog(n))
        Worst Case Time Complexity:     O(nlog(n))
        Worst Case Space Complexity:    O(n)

    Pros:
        - Most implementations are stable
            Stable sorts maintain the original order of equal elements
            This is useful in the case that satalite data is stored with these elem.
        - Faster than quicksort and heapsort for linked lists

    Cons:
        - High space Complexity
        - Does not sort in-space
        - Slower on average than Quicksort
        - More space than Heapsort
    """

    if len(l) <= 1:  #Base case: 0 or 1 len list is just returned
        return l

    middle = len(l)/2  #The pivot point for the merge 

    left = mergesort(l[:middle])  #recursive call to continue to branch into 1 ele leaves
    right = mergesort(l[middle:])

    return list(merge(left, right))  #Heapq's merge concatenates our 1-elem. lists in sorted order. 



