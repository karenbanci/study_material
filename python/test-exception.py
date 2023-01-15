print("Hi")

try:
    a = 7 / "oi"
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception:
    print("Error: Something went wrong")

print("Bye")


try:
    items = ['a', 'b']
    third = items[2]
except IndexError:
    print("list index out of range on line 2")


try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e:
    print("got an error")
    print(e)

print("continuing")

print(5* "----")

def main():
  try:
    A()
  except ZeroDivisonError:
    # execute if a ZeroDivisonError message happened
    print("Error: Cannot divide by zero")

    def A():
        B()

    def B():
        C()

    def C():
        D()

    def D():
    # processing code
        if something_special_happened:
            raise ZeroDivisonError
