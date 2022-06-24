// import MinHeap class
const MinHeap = require("./MinHeap");

// instantiate a MinHeap class
const minHeap = new MinHeap();

// helper function to return a random integer
const randomize = () => Math.floor(Math.random() * 40);

// populate minHeap with random numbers
for (let i = 0; i < 6; i++) {
  const num = randomize();
  console.log(`.. Adding value ${num}`);
  minHeap.add(num);
  console.log("Content of min-heap", minHeap.heap);
}

// return the minimum value in the heap until heap is empty
console.log("\n");
for (let i = 0; i < 6; i++) {
  console.log(`.. Removing minimum value ${minHeap.popMin()}`);
  console.log("Content of min-heap", minHeap.heap);
}
