"""
1. Append Size
For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:

Define the function to accept one parameter for our list
Get the length of the list
Append the length of the list to the end of the list
Return the modified list
"""

def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))


"""
2. Append Sum
Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. Here are the steps we need:

Define the function to accept one parameter for our list of numbers
Add the last and second to last elements from our list together
Append the calculated value to the end of our list.
Repeat steps 2 and 3 two more times
Return the modified list
"""

def append_sum(lst):
    for n in range(3):
        lst.append(lst[-1] + lst[-2])
    return lst


print(append_sum([1, 1, 2]))

"""
3. Larger List
Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists. Here are the steps:

Define the function to accept two parameters for our two lists of numbers
Check if the length of the first list is greater than or equal to the length of the second list
If true, then return the last element from the first list. Otherwise, return the last element from the second list

"""

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
print(larger_list([4, 10, 2, 5, 3], [-10, 2, 5, 10]))
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10, 4, 6]))


"""
4. More Than N
Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type. We have a conveyor belt full of different types of snacks represented by different numbers. Our function will accept a list of numbers (representing the type of snack), a number for the second parameter (the type of snack we are looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). The function will return True if the snack we are searching for appears more times than we provided as our third parameter. These are the steps we need:

Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances
Count the number of occurrences of item (the second parameter) in lst (the first parameter)
If the number of occurrences is greater than n (the third parameter), return True. Otherwise, return False
"""

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

"""
5. Combine Sort
Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:

Define the function to accept two parameters, one for each list.
Combine the two lists together
Sort the result
Return the sorted and combined list
"""

def combine_sort(lst1, lst2):
  return sorted(lst1 + lst2)

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
