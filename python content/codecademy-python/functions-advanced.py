"""
1. First Three Multiples
Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number. For this, we are going to need a few steps:

Define the function header to accept one input parameter called num
Print out 1 times num
Print out 2 times num
Print out 3 times num
Return the value of 3 times num

"""

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

"""
2. Tip
Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. This function will accept both of those values as inputs and return the amount of money to tip. In order to do this, we will need a few steps:

Define the function to accept the total cost of the food called total and the percentage to tip as percentage
Calculate the tip amount by multiplying the total and percentage and dividing by 100
Return the tip amount
"""
def tip(total, percentage):
  return (total * percentage) / 100

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

"""
3. Bond, James Bond
It’s time to re-create a famous movie scene through code. Our function is going to concatenate strings together in order to replace James Bond’s name with whatever name we want. The input to our function will be two strings, one for a first name and another for a last name. The function will return a string consisting of the famous phrase but replaced with our inputs. To accomplish this, we need to:

Define the function to accept two parameters, first_name and last_name
Concatenate the string ', ' on to the last_name
Concatenate the first_name on to the result of the previous step
Concatenate a space on to the result
Concatenate the last_name again to the result
Return the final string
"""
def introduction(first_name, last_name):
  return last_name + ', ' + first_name + ' ' + last_name

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

"""
4. Dog Years
Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age. This will require a few steps:

Define the function called dog_years to accept two parameters: name and age
Calculate the age of the dog in dog years
Concatenate the string with the dog’s name and age in dog years
Return the resulting string
"""

def dog_years(name, age):
  return name + ', you are ' + str(age * 7) + ' years old in dog years'

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

"""
5. All Operations
For the final code challenge, we are going to perform multiple mathematical operations on multiple inputs to the function. We will begin with adding the first two inputs, then we will subtract the third and fourth inputs. After that, we will multiply the first result and the second result. In the end, we will return the remainder of the previous result divided by the first input. We will also print each of the steps. The steps needed to complete this are:

Define the function to accept four inputs: a, b, c, and d
Print and store the result of a + b
Print and store the result of c - d
Print and store the first result times the second result
Return the previous result modulo a
"""
def lots_of_math(a, b, c, d):
  print(a + b)
  print(c - d)
  print((a + b) * (c - d))
  return (a + b) * (c - d) % a

print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

