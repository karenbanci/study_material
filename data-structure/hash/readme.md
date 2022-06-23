font: codecademy

# Hash Map

## Intro to Hash Maps

Hash maps are data structures that serve as efficient key-value stores. They are capable of assigning and retrieving data in the fastest way possible. This is because the underlying data structure that hash maps use is an array.

A value is stored at an array index determined by plugging the key into a hash function. Because we always know exactly where to find values in a hash map, we have constant access to any of the values it contains.

This quick access to values makes a hash map a good choice of data structure whenever we need to store a lot of values but need fast look-up time.

In JavaScript, objects are often used to map keys to values as in a hash map, but in this lesson, you’ll create your own implementation of a hash map by building out a HashMap class. You’ll build methods to hash and compress a given key, assign an index at which to store a value, and retrieve that value.

To implement a hash map, the HashMap constructor method will create an empty array that will hold values. A hashing function will return an index in the array where the value will be stored. While going through the following exercises, remember that the purpose of this lesson is to gain a deeper understanding of the data structure rather than creating a production-quality data structure.

## Hashing

The hashing function is the secret to efficiently storing and retrieving values in a hash map. A hashing function takes a key as input and returns an index within the hash map’s underlying array.

This function is said to be deterministic. That means the hashing function must always return the same index when given the same key. This is important because we will need to hash the key again later to retrieve the stored value. We won’t be able to do this unless our hashing function behaves in a predictable and consistent way.

Getting an integer representing an index can be done by summing up each character code of the key (as a numeric value) with the running total of the previously summed character codes.

The hashing function should follow this logic:

declare hashCode variable with value of 0

for each character in the key
  add the sum of the current character code value and hashCode to hashCode

return hashCode
Adding the sum of hashCode and the character code to the hashCode again creates a deterministic and also non-reversible implementation of a hashing function. This avoids generating a duplicate index if keys have the same characters in different orders, such as bat and tab.

## Compression

The current hashing function will return a wide range of integers — some of which are not indices of the hash map array. To fix this, we need to use compression.

Compression means taking some input and returning an output only within a specific range.

In our hash map implementation, we’re going to have our hashing function handle compression in addition to hashing. This means we’ll add an additional line of code to compress the hashCode before we return it.

The updated .hash() should follow these steps:

initialize hashCode variable to 0

for each character in the key
   add the character code and hashCode to hashCode

return compressed hashCode

## Assign

We now have everything we need to find a place in the hash map array to store a value. The only thing left to do is assign the value to the index we generated. A method, .assign() will handle the logic needed to take in a key-value pair and store the value at a particular index.

A general outline of how .assign() will work is this:

store the hashed key in a variable arrayIndex
assign the value to the element at arrayIndex in the hash map

## Retrieve

To be a fully functional hash map, we have to be able to retrieve the values we are storing. To implement retrieval for our hash map we’ll create a new HashMap method, .retrieve().

This method will make use of .hash()‘s deterministic nature to find the value we’re looking for in the hash map.

## Collisions

We have a hash map implementation, but what happens when two different keys generate the same index? Run the code in collision.js to see a collision in action.

Instead of returning 'marsh plant' and 'forest animal' we retrieve 'forest animal' twice. This is because both key-value pairs are assigned to the same index 0 and the first value, 'marsh plants' was overwritten.

When two different keys resolve to the same array index this is called a collision. In our current implementation, all keys that resolve to the same index are treated as if they are the same key. This is a problem because they will overwrite one another’s values.

## Collisions: Assigning

Our first step in implementing a collision strategy is updating our constructor and .assign() method to use linked lists and nodes inside the hashmap array. This will allow us to store multiple values at the same index by adding new nodes to a linked list instead of overwriting a single value. This strategy of handling collisions is called separate chaining.

A collision-proof .assign() should look like this to start:

store the hashed key in a variable arrayIndex
store linked list at arrayIndex in a variable linkedList

if linked list is empty
  add the key-value pair to the linked list as a node
We’ll be using the LinkedList and Node classes found in the LinkedList.js and Node.js files to implement our collision-proof HashMap class. The only file you will be working in for this exercise is HashMap.


## Collisions: Looping

We’ve added code to .assign() that takes care of an empty list, but what happens when there is a collision and there are already values stored at a particular index?

If there are already values stored in nodes at an index, we need to loop over each node in the list in order to determine how to proceed.

The two possibilities we’ll encounter while looping are:

The key we are looking for and the key of the current node is the same, so we should overwrite the value

No node in the linked list matches the key, so we should add the key-value pair to the list as the tail node

After both cases, if we haven’t already exited the loop, we should reset the loop’s condition.

With this in mind, the .assign() code for looping should look like this:

store the head node of the linked list in a variable current

while there is a current node
  if the current node's key is the same as the key
    store the key and value in current
  if the current node is the tail node
    store the key-value pair in the node after current
    exit the loop
  set current to the next node

## Collisions: Retrieving

When we retrieve hash map values, we also need to be aware that different keys could point to the same array index leading us to retrieve the wrong value.

To avoid this, we’ll search through the linked list at an index until we find a node with a matching key. If we find the node with the correct key, we’ll return the value; otherwise, we’ll return null.

The .retrieve() method will follow this logic:

store the hashed key in the constant arrayIndex
store the head node of a list in the variable current

while there is a valid node
  if the current node's key matches the key
    return the current node's value
  set current to the next node in the list

return null
