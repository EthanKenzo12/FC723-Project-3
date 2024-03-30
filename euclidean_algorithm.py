def euclidean_algorithm(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two positive integers using the Euclidean Algorithm.

    Parameters:
    a (int): a positive integer representing the dividend.
    b (int): a positive integer representing the divisor.

    Returns:
    int: The GCD of a and b.
    """

    # If b is 0, a is the GCD
    if b == 0:
        return a

    # If b is greater than a, swap a and b
    if b > a:
        a, b = b, a

    # Recursively apply the Euclidean Algorithm
    return euclidean_algorithm(b, a % b)


# Example usage
# The GCD of 48 and 18 is 6
print(euclidean_algorithm(48, 18))