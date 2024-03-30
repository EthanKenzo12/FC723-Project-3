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


# created try exception handling to give the user an error message if the input is invalid
try:
    # prompt for user input for the values of a and b
    a = int(input("Give me a value for a: "))
    b = int(input("Give me a value for b: "))

    print(euclidean_algorithm(a, b))
except ValueError:
    """
    Exception handling occurs if the user enters something that cannot be converted to an integer,
    such as a string or a float.
    Example: twenty-one or 21.0 instead of 21
    
    """
    print("Error: Please enter a positive integer and try again!")
except RecursionError:
    """
    Exception handling occurs if the recursive calls exceed the maximum recursion depth
    this may be done if there is a negative value for a and a positive value for b.
    Example: -40 and 2
    """
    print("Error: Recursion limit exceeded please try again!")
