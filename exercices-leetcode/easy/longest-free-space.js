/*
Return longest a free space

input = [Free, Taken, Free, Free]
outuput = 2

input = [Free, Taken]
outuput = 1

input = [Free, Free, Free, Taken, Free, Free]
outuput = 3

Use just only 1 loop.
Another data structure is not necessary, I can't use stack ou queue or nothing


input = [Free, Free, Free, Taken, Free, Free]
Iteractions
index[0] = Free +1
index[1] = Free +1
index[2] = Free +1
index[3] = Taken
index[4] = Free +1
index[5] = Free +1



*/

var findLengthOfLCIS = function (arr) {
  if (arr.length === 0) return 0;
  let result = 1;
  for (let i = 0; i < arr.length - 1; i++) {
    let j = i + 1;
    while (j < arr.length && arr[j] > arr[j - 1]) {
      j++;
    }
    result = Math.max(result, j - i);
  }
  return result;
};

const arr = ["Free", "Free", "Free", "Taken", "Free", "Free"];
console.log(findLengthOfLCIS(arr));
