"""
1. Check Name
You are creating an app that allows users to interact and share their coding project ideas online. The first step is to provide your name in the application and a greeting for other people to see which contains your name. Let’s create a function that is able to check if a user’s name is located within their greeting. We need a function that accepts two parameters, a string for our sentence and a string for a name. The function should return True if the name exists within the string (ignoring any differences in capitalization). Here is what we need to do:

Define the function to accept two parameters, one string for the sentence and one string for the name
Convert all of the strings to the same case so we don’t have to worry about differences in capitalization
Check if the name is within the sentence. If so, then return True. Otherwise, return False
"""

def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False

print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

"""
2. Every Other Letter
For this next function, we are going to create a function that extract every other letter from a string and returns the resulting string. There are a few different ways you can solve this problem Here are the steps needed for one of the ways:

Define the function to accept one parameter for the string
Create a new empty string to hold every other letter from the input string
Loop through the input string while incrementing by two every time
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the new string
"""
def every_other_letter(word):
  new_string = ''
  for i in range(0, len(word), 2):
    new_string += word[i]
  return new_string

print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

"""
3. Reverse
This one is similar to the last challenge. Instead of selecting every other letter, we want to reverse the entire string. This can be performed in a similar manner, but we will need to modify the range we are using. Here is what we need to do:

Define the function to accept one parameter for the string
Create a new empty string to hold the reversed string
Loop through the input string by starting at the end, and working towards the beginning
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the result
"""

def reverse(string):
  new_string = ''
  for i in range(len(string) - 1, -1, -1):
    new_string += string[i]
  return new_string

print(reverse("Codecademy"))
# should print ymedacedoC
print(reverse("Hello world!"))
# should print !dlrow olleH
print(reverse(""))
# should print

"""
4. Make Spoonerism
A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”. We are going to make a function that is similar, but instead of using the first syllable, we are going to switch the first character of two words. Here is what we need to do:

Define the function to accept two parameters for our two words
Get the first character of the first word and the first character of the second word
Get the remaining characters of the first word and the remaining characters of the second word.
Append the first character of the second word to the remaining character of the first word
Append a space character
Append the first character of the first word to the remaining characters of the second word.
Return the result

"""
def make_spoonerism(word1, word2):
  new_word1 = word2[0] + word1[1:]
  new_word2 = word1[0] + word2[1:]
  return new_word1 + ' ' + new_word2

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

""""
5. Add Exclamation
Let’s say we are writing a program that displays a large message on a blimp and we need to fill in any missing space if a short phrase is provided. Our function will accept a string and if the size is less than 20, it will fill in the remaining space with exclamation marks until the size reaches 20. If the provided string already has a length greater than 20, then we will simply return the original string. Here are the steps:

Define the function to accept one parameter for our string
Loop while the length of our input string is less than 20
Inside the loop, append an exclamation mark
Once done, return the result
"""
def add_exclamation(word):
  while len(word) < 20:
    word += '!'
  return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
