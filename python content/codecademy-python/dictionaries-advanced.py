"""
1. Word Length Dict
Let’s start by writing a function that creates a new dictionary based on a list of strings. The keys of our dictionary will be every string in our list of strings, while the values will be the length of each of the words in the string list. Here are the steps:

Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, add the string as a key and the length of the string as the value to the dictionary
After the loop, return the new dictionary
"""

def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog":3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a":1, "":0}

"""
2. Frequency Count
This next function is similar, but instead of counting the length of each string in the list of strings, we will be counting the frequency of each string. This function will also accept a list of strings as input and return a new dictionary. Here is what we need to do:

Define the function to accept one parameter for our list of strings
Create a new empty dictionary
Loop through every string in the list of strings
Inside the loop, if the string is not already in our dictionary, store the string as a key with a value of 0 in our dictionary. Then, increment the value by 1.
After the loop, return the new dictionary
"""
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

"""
3. Unique Values
Now let’s try reading a dictionary as input and finding how many values are unique. The function should return a number which is the count of all values from the dictionary without including duplicates. These are the steps:

Define the function to accept one parameter for our dictionary
Create a new empty list
Loop through every value in our dictionary
Inside the loop, if the value is not already in our list, append the value to our list
After the loop, return the length of our list
"""

def unique_values(my_dictionary):
  values = []
  for value in my_dictionary.values():
    if value not in values:
      values.append(value)
  return len(values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


"""
4. Count First Letter
This function accepts a dictionary where the keys are last names and the values are lists of first names of people who have that last name. We need to calculate the number of people who have the same first letter in their last name. Here are the steps we need:

Define the function to accept one parameter for our dictionary
Create a new empty dictionary called letters
Loop through every key in our names dictionary
Inside the loop, get the first letter of the last name we are looking at. If the first letter is not in our letter dictionary, add it as a key with a value of 0. Then, increment that key by the number of people that have that last name
After the loop, return the letters dictionary
"""
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {'S': 4, 'L': 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"], "Targaryen": ["Daenerys", "Viserys", "Rhaegar"]}))
# should print {'S': 4, 'L': 3, 'T': 3}

