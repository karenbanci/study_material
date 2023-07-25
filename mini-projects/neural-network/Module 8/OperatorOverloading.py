import LinkedList


class Employee:
    def __init__(self, first: str, last: str, number: int):
        self._first = first
        self._last= last
        self._number = number

    def __str__(self):
        ret_val = f"Employee Number: {self._number}\n"
        ret_val += f"Name: {self._first}"
        return ret_val

    def __eq__(self, other):
        if isinstance(other, int):
            return self._number == other
        return self == other


me = Employee("Karen", "Banci", 12345)
print(me == 12345)
# print(me)
"""
Employee Number: 12345
Name: Karen
"""

you = Employee( "Jairo", "Honorio", 67890)
# print(you)
"""
Employee Number: 67890
Name: Jairo
"""

my_list = LinkedList.LinkedList()
my_list.add_to_head(me)
my_list.add_to_head(you)
result = my_list.find(12345)
print(result)
result = my_list.find(34567)
print(result)