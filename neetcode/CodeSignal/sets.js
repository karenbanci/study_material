/**
 * Alright, Space Voyager, picture this: You've been assigned a crew and each member has a unique ID consisting of alphanumeric characters. Now, you're sifting through these IDs and need to find the first one that appears more than once in the array. If every ID unique or the array is empty, just return an empty string.

Now go on, rocket your solution to this! And don't forget, the answer format should be a string - that string is our elusive doubled ID or an empty string if we find no doubles in the array. Make it shine, Voyager!
 */

function findFirstDuplicateID(ids) {
  let idSet = new Set();

  // TODO: Find an id that appears more than once and return it
  // monitor of duplicates
  let duplicatesSet = new Set();

  // iterate the id array, filling idSet and duplicatesSet
  for (let id of ids) {
    // console.log(id);
    if (idSet.has(id)) {
      duplicatesSet.add(id);
    } else {
      idSet.add(id);
    }
  }
  // console.log("duplicatesSet", duplicatesSet);

  if (duplicatesSet) {
    return duplicatesSet.values().next().value;
  }
  // Return an empty string if no duplicate ids are found
  return "";
}

console.log(
  findFirstDuplicateID(["X123", "A456", "X123", "B789", "A456", "C111"])
); // Expected "X123"
console.log(findFirstDuplicateID(["Z999", "Y888", "Z999", "Y888"])); // Expected "Z999"
console.log(
  findFirstDuplicateID(["E100", "B200", "C300", "E100", "D400", "C300"])
); // Expected "E100"
