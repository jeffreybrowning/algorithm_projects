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

def simple_merge(l1, l2):
    """A simple implementation of the merge function provided by Python in the
    heapq module. 

    Merge has the following steps:

        1.  Determine that the first list is non-empty (base case)
        2.  Determine that the second list is non-empty (base case)
        3.  Determine which is larger, l1[0] or l2[0]?
        4.  If l1[0] is larger, add it to a new list and rerun merge on the 
            rest of l1 and l2. If l2[0] is larger, add it to the new list instead 
            and call merge recursively as before. 
    """

    if l1 == [] and l2 == []:
        return []
    elif l1 == []:
        return l2
    elif l2 == []:
        return l1

    if l1[0] <= l2[0]:
        return [l1[0]] + simple_merge(l1[1:], l2)
    else:
        return [l2[0]] + simple_merge(l2[1:], l1)
