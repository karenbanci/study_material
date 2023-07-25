
def reverse_a_string(input_str: str):
    """ reverse a string recursively"""
    if len(input_str) == 1:
        return input_str
    first_letter = input_str[-1]
    remainder_reserved = reverse_a_string(input_str[:-1])
    return first_letter + remainder_reserved


print(reverse_a_string("python"))


def fibonacci(n: int):
    # Fibonacci
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\n", fibonacci(7))