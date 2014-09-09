def binarysearch(x, l):
    if l == []:
        return False
    if l[0] == x:
        return True

    middle = len(l)/2 

    if l[middle] == x:
        return True
    if x > l[middle]:
        return binarysearch(x, l[middle:])
    if x < l[middle]:
        return binarysearch(x, l[:middle])
