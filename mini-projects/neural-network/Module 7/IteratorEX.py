"""
Iterable is a class tha implements a method called hitter and
it should return and iterator object.
"""

my_list = [10, 8, 6, 4, 2]
print(my_list.__dir__()) # prints all methods tha I can use in my_list

# my_iter = my_list.__iter__()
# print(type(my_iter)) # returned an object
# print(my_iter)

# my_iter = my_list.__iter__()
# print(my_iter.__next__()) # we got the number 10
# print(my_iter.__next__()) # we got the number 8
# print(my_iter.__next__()) # we got the number 6
# print(my_iter.__next__()) # we got the number 4
# print(my_iter.__next__()) # we got the number 2

""""
My list is iterable because ir implements the iter method,
that returns and iterator implements both.
"""
my_iter = iter(my_list)
print(next(my_iter))    # we got the number 10
print(next(my_iter))    # we got the number 8
print(next(my_iter))    # we got the number 6
print(next(my_iter))    # we got the number 4
print(next(my_iter))    # we got the number 2

