def eulers_algorithm(x, y):
    """Returns the greatest common factor, GCF, of two integers.
    Euler's algorithm recursively attempts to minimize the remain-
    -der of the modulus operation on the two numbers, eventually 
    yeilding the number that results in a zero remainder modulus
    operation.
    """

    if y == 0:
       return x
    else:
       return eulers_algorithm(y, x % y)