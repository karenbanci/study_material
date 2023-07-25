def our_range(start, stop):
    curr = start
    while not curr == stop:
        yield curr
        curr += 1


# for i in our_range(0,10):
#     print(i)
"""
output
0
1
2
3
4
5
6
7
8
9
"""

# or we can do this
# range_obj = our_range(0,10)
# print(range_obj.__dir__())
"""
output
['__repr__', '__getattribute__', '__iter__', '__next__', '__del__', 'send', 
'throw', 'close', 'gi_frame', 'gi_running', 'gi_code', '__name__', 
'__qualname__', 'gi_yieldfrom', '__doc__', '__hash__', '__str__', 
'__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', 
'__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', 
'__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', 
'__dir__', '__class__']
"""

def fib(n):
    prev = 1
    last = 1
    for count in range(n):
        if count == 0 or count == 1:
            yield 1
            continue
        curr = prev + last
        yield curr
        prev, last = last, curr


for a in fib(10):
    print(a)

"""
output
1
1
2
3
5
8
13
21
34
55
"""