"""
1. Larger Sum
We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

Define the function to accept two input parameters: lst1 and lst2
Create two variables to record the two sums
Loop through the first list and add up all of the numbers
Loop through the second list and add up all of the numbers
Compare the first and second sum and return the list with the greater sum
"""

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))
# Should print [1, 9, 5] because it has the larger sum: 15


"""
2. Over 9000
We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this, we will need the following steps:

Define the function to accept a list of numbers
Create a variable to keep track of our sum
Iterate through every element in our list of numbers
Within the loop, add the current number we are looking at to our sum
Still within the loop, check if the sum is greater than 9000. If it is, end the loop
Return the value of the sum when we ended our loop
"""

def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if sum > 9000:
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))
# Should print 9020

"""
3. Max Num
Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

Define the function to accept a list of numbers called nums
Set our default maximum value to be the first element in the list
Loop through every number in the list of numbers
Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
Return the maximum number
"""

def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max

print(max_num([50, -10, 0, 75, 20]))
# Should print 75

"""
4. Same Values
In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index. These are the steps we need to accomplish this:

Define our function to accept two lists of numbers
Create a new list to store our matching indices
Loop through each index to the end of either of our lists
Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
Return our list of indices
"""

def same_values(lst1, lst2):
  indices = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      indices.append(index)
  return indices

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# Should print [0, 2, 3]

"""
5. Reversed List
For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list. Here is what you need to do:

Define a function that has two input parameters for our lists
Loop through every index in one of the lists from beginning to end
Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return False
If the loop ended successfully, then we know the lists are reversed and we can return True.
"""

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
# Should print True
print(reversed_list([1, 5, 3], [3, 2, 1]))
# Should print False
