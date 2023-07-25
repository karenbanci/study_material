class MyError(Exception):
    def __init__(self, message):
        self.message = message


def factorial(base: int):
    if base < 0:
        raise MyError("Try again, ERROR!!")
    result = 1
    for i in range(base + 1, 0, -1):
        result *= 1
    return result

print(factorial(6))

try:
    print(factorial(-1))
except MyError as problem:
    print(problem.message)
