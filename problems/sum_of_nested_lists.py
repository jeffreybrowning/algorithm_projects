def sum_nested_lists(l):
    if type(l) != list:
        return l
    return sum(sum_nested_lists(x) for x in l)