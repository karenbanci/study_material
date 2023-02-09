"""
1. Sum Values
For the first code challenge, we are going to look at only the values in a dictionary. This function should sum up all of the values from the key-value pairs in the dictionary. Here are the steps we need:

Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every value in the dictionary
Inside the loop, add each value to the sum
Return the sum
"""
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

"""
2. Even Keys
Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values. Additionally, we are going to only look at every even key within the dictionary. Here are the steps:

Define the function to accept one parameter for our dictionary
Create a variable to keep track of our sum
Loop through every key in the dictionary
Inside the loop, if the key is even, add the value from the even key
After the loop, return the sum
"""
def sum_even_keys(my_dictionary):
  sum = 0
  for key, val in my_dictionary.items():
    if key % 2 == 0:
      sum += val
  return sum

# OR

def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

"""
3. Add Ten
Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our function should add 10 to every value in the dictionary and return the modified dictionary. Here is what we need to do:

Define the function to accept one parameter for our dictionary
Loop through every key in the dictionary
Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
After the loop, return the modified dictionary
"""

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

"""
4. Values That Are Keys
We are making a program that will create a family tree. Using a dictionary, we want to return a list of all the children who are also parents of other children. Using dictionaries we can consider those people to be values which are also keys in our dictionary of family data. Here is what we need to do:

Define the function to accept one parameter for our dictionary
Create an empty list to hold the values we find
Loop through every value in the dictionary
Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the list of values we found
After the loop, return the list of values which are also keys
"""
def values_that_are_keys(my_dictionary):
  values = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      values.append(value)
  return values

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

"""
5. Largest
For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary and return the associated key. This is a twist on the max algorithm since it is using a dictionary rather than a list. These are the steps:

Define the function to accept one parameter for our dictionary
Initialize the starting key to a very low number
Initialize the starting value to a very low number
Iterate through the dictionary’s key/value pairs.
Inside the loop, if the current value is larger than the current largest value, replace the largest key and largest value with the current ones you are looking at
Once you are done iterating through all key/value pairs, return the key which has the largest value
"""

def max_key(my_dictionary):
  largest_key = 0
  largest_value = 0
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

