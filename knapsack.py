class Memoize:
    def __init__(self, function):
        self.function = function
        self.values = {}
    def __call__(self, *args):
        if not args in self.values:
            self.values[args] = self.function(*args)
        return self.values[args]

def backpack(items, weight):
    '''Solves 0,1 backpack problem. Returns the maximum
    sum of the values of items whose collective weight is less 
    than or equal to the weight provided.

    items is a list of value, weight tuples. 

    weight is the max weight of items that fit in our bag. weight
    must be a positive integer. 
    '''

    @Memoize
    def dp(i, j):
        if i == 0:
            return 0
        if items[i][1] <= j:
            current_max = max(dp(i-1, j), dp(i-1, j-items[i][1]) + items[i][0])
        else:
            current_max = dp(i-1, j)
        return current_max

    n = len(items)
    for i in range(1, n):
        for j in range(weight):
            maximum = dp(i,j)
    return maximum

#items = [(5, 9), (3, 1), (2, 1), (6, 6), (2, 2)]
#w = 15
#print backpack(items, w)