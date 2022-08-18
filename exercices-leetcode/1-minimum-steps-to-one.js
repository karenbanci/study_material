// function minimumStepsToOne(num) {
//   let count = 0;
//   const sub = num - 1;
//   const divBy3 = num / 3;
//   const divBy2 = num / 2;

//   if (num % 5 == 0) {
//     while(count != 0){
//       sub;
//       count++;
//       divBy3;
//       count++;
//     }
//   }
//   if (num % 2 == 0) {
//     while(count != 0){
//       divBy2;
//       count++;
//     }
//   }

//   if (num % 3 == 0) {
//     while(count != 0){
//       divBy3;
//       count++;
//     }
//   }

//   return count;
// }

// const num = 10;
// // const num = 4;

// console.log(minimumStepsToOne(num));


let bcount = 0;
function minStepsToOne(n) {
  bcount++;
  // Base case
  if (n === 1) {
    return 0;
  }

  // Recursive relations
  // sub1
  let steps = minStepsToOne(n - 1);

  // divby2
  if (n % 2 === 0) {
    let divby2 = minStepsToOne(n / 2);
    steps = Math.min(steps, divby2);
  }

  // divby3
  if (n % 3 === 0) {
    let divby3 = minStepsToOne(n / 3);
    steps = Math.min(steps, divby3);
  }

  // min steps to one from n
  let result = 1 + steps;
  // console.log(n, result);
  return result;
}

let cache = {};
let mcount = 0;
function minStepsToOneMemo(n) {
  mcount++;
  // Base case
  if (n === 1) {
    return 0;
  }
  // Check cache for repeated state
  if (n in cache) {
    return cache[n];
  }

  // Recursive relations
  // sub1
  let steps = minStepsToOneMemo(n - 1);

  // divby2
  if (n % 2 === 0) {
    let divby2 = minStepsToOneMemo(n / 2);
    steps = Math.min(steps, divby2);
  }

  // divby3
  if (n % 3 === 0) {
    let divby3 = minStepsToOneMemo(n / 3);
    steps = Math.min(steps, divby3);
  }
  // min steps to one from n
  let result = 1 + steps;

  // store result for n in cache
  cache[n] = result;
  return result;
}

function minStepsToOneTab(n) {
  // init tab data structure
  let tab = new Array(n + 1);

  // apply base case to tab
  tab[1] = 0;

  // loop tab, filling subproblem solns
  for (let i = 2; i <= n; i++) {
    // sub1
    let steps = tab[i - 1];
    // divby2
    if (i % 2 === 0) {
      let divby2 = tab[i / 2];
      steps = Math.min(steps, divby2);
    }
    // divby3
    if (i % 3 === 0) {
      let divby3 = tab[i / 3];
      steps = Math.min(steps, divby3);
    }
    // min steps to one from i
    let result = 1 + steps;
    // store result for i in tab
    tab[i] = result;
  }
  // return min steps to 1 from n
  return tab[n];
}

console.time(`Brute force recursion`);
console.log(minStepsToOne(400));
// console.timeEnd(`Brute force recursion`);
// console.log(`Call count :${bcount}`);

// console.time(`Memoization`);
// console.log(minStepsToOneMemo(400));
// console.timeEnd(`Memoization`);
// console.log(`Call count :${mcount}`);

// console.time(`Tabulation`);
// console.log(minStepsToOneTab(10));
// console.timeEnd(`Tabulation`);
