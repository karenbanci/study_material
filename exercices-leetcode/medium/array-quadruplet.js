/*
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9]

sorted = arr = [0,1, 2, 3, 4, 5, 7, 9]
                i
                  j
                                low
                                   high

        arr[i], arr[j]
        (i < j)

sum = 20 ( find two subarry such that their sum equals to `result = s - (arr[i], arr[j])`)
*/

function findArrayQuadruplet(arr, s) {

  //sorted by ascendent
  const sorted = arr.sort();
  console.log(sorted);
  //size of array
  const size = sorted.length;

  // if size be less than 4, return empty array
  if(size < 4) return [];

  // here we can initialize loop for 2 points
  for(let i = 0; i < size - 4; i++) {
    for(let j = i+1; j < size - 3; j++){

      const result = s - (sorted[i] + sorted[j]);
      console.log("result: "+ result)

      //this points (low and high) that initially point to two end-points of the subarray
      const [low, high] = [sorted[j + 1], sorted[size - 1]];

      while(low < high){
        //reduce the search space arr[low...high] at each iteration of the loop
        if (sorted[low] + sorted[high] < result) {
          //increment low if the sum is less than r
          low++;
        } else if (sorted[low] + sorted[high] > result) {
          //decrement high if the sum is more than r
          high--;
        } else {
          //if the sum is equal to r, we found the desired pair
          return [sorted[i], sorted[j], sorted[low], sorted[high]];
        }
      }
    }
  }
  return []
}

//output: [0, 4, 7, 9]
const arr = [0, 1, 2, 3, 4, 5, 7, 9];
const s = 20;
console.log(findArrayQuadruplet(arr, s));


/*
Time: O(N^3)
Space: O(1)

The naive solution would be to consider every quadruplet in the input array and return the one (if exists) whose sum is s. This approach requires using 4 nested loops and its time complexity is O(N^4). This is quite inefficient and we can do better than that.

We start by sorting the given array in ascending order and then for each pair (arr[i], arr[j]) in the array where (i < j), we check if a quadruplet is formed by current pair and a pair from a subarray arr[j+1...n-1]. So how do we find a complementing pair in the subarray arr[j+1...n-1]?

What we want to do is to find two values in the subarray such that their sum equals to s - (arr[i], arr[j]). Let’s denote this value as r. Now, since we made sure to sort arr in an ascending order, the idea is to maintain the search space by keeping two indexes (low and high) that initially point to two end-points of the subarray. Then we loop until low is less than high and reduce the search space arr[low...high] at each iteration of the loop. We compare the sum of the values present at index low and high with r and increment low if the sum is less than r and decrement high if the sum is more than r. Finally, if the sum is equal to r, we found the desired pair.

The quadruplet will then consist of the initial pair we found in the first step and the complementing pair we found in the subarray. */
